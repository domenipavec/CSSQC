#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/__init__.py
# 
# css quality control
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import argparse, configparser, pkgutil, os.path, importlib

import cssqc.rules
from pkg_resources import resource_string
import cssqc.parser

def main():
    """Entry point for the application script"""
    parser = argparse.ArgumentParser(description="""Check quality of css or less files.
Rule options on command line override those in configuration file.
All rule options (OPT) can be either 'on' or 'off' or one of specified options.""")
    parser.add_argument('--input', '-i', nargs='+', type=argparse.FileType('r'), help='Input css or less file(s).', required=True)
    parser.add_argument('--config', '-c', help='Configuration file.', type=argparse.FileType('r'))
    parser.add_argument('--verbose', '-v', help='More verbose output with some statistics.', action='store_true')
    
    rules = []
    
    pkgpath = os.path.dirname(cssqc.rules.__file__)
    for _, rule, _ in pkgutil.iter_modules([pkgpath]):
        try:
            module = importlib.import_module("cssqc.rules."+rule)
            method = getattr(module, "getHelp")
            parser.add_argument('--'+rule, help=method(), metavar='OPT')
            rules.append(rule)
        except:
            pass
    
    args = parser.parse_args()
    
    config = configparser.ConfigParser()
    config.optionxform = lambda option: option
    config.read_string(resource_string(__name__, 'defaults.cfg').decode('utf-8'))
    
    if args.config is not None:
        config.read_file(args.config)

    for rule in rules:
        if getattr(args, rule) is not None:
            config.set('RULES', rule, getattr(args, rule))

    report = []

    for i in args.input:
        parser = cssqc.parser.CSSQC(config['RULES'])
        
        try:
            parser.parse(i.read())
        except Exception as e:
            print('Error in "%s":' % i.name, str(e))
            if args.verbose:
                raise e
            exit()
        
        for w in parser.warnings:
            print('Warning: Rule "%s" broken on line %d in "%s".' %(w.rule, w.line, i.name))
            if args.verbose:
                print('         ' + w.message)

        lines = parser.tokens[-1].lineno
        warnings = len(parser.warnings)
        q = (1.-float(warnings)/parser.statistics.properties.total)*100
        if args.verbose:
            report.append('File "%s":' % i.name)
            report.append('  Lines:      %4d' % lines)
            report.append('  Warnings:   %4d' % warnings)
            report.append('  Quality:    %7.2f' % q)
            report.append('  IDs:        %4d styled,    %4d unique' % parser.statistics.ids.pair())
            report.append('  Classes:    %4d styled,    %4d unique' % parser.statistics.classes.pair())
            report.append('  Tags:       %4d styled,    %4d unique' % parser.statistics.tags.pair())
            report.append('  Selectors:  %4d used,      %4d unique' % parser.statistics.selectors.pair())
            report.append('  Properties: %4d specified, %4d unique' % parser.statistics.properties.pair())
        else:
            report.append('File "%s": %d warnings on %d lines (q=%.2f)' %(i.name, warnings, lines, q))
    
    print('===================================================================')
    print('\n'.join(report))

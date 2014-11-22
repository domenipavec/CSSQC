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
    parser.add_argument('--verbose', '-v', help='More verbose output.', action='store_true')
    
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
        parser.parse(i.read())
        
        for w in parser.warnings:
            print('Warning: Rule "%s" broken on line %d in "%s".' %(w.rule, w.line, i.name))
            if args.verbose:
                print('         ' + w.message)

        lines = parser.tokens[-1].lineno
        warnings = len(parser.warnings)
        report.append('File "%s": %d warnings on %d lines (q=%.2f)' %(i.name, warnings, lines, (1.-float(warnings)/lines)*100)) 
    
    print('===================================================================')
    print('\n'.join(report))

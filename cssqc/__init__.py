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

import importlib
import csslex, cssyacc

EVENTS = (
    'IDENT',
    'ATKEYWORD',
    'ATBRACES',
    'STRING',
    'HASH',
    'NUMBER',
    'PERCENTAGE',
    'DIMENSION',
    'URI',
    'UNICODE_RANGE',
    'CDO',
    'CDC',
    'COLON',
    'SEMICOLON',
    'BRACES_R',
    'BRACES_L',
    'PARENTHESES_R',
    'PARENTHESES_L',
    'BRACKETS_R',
    'BRACKETS_L',
    'COMMENT',
    'WS',
    'FUNCTION',
    'INCLUDES',
    'DASHMATCH',
    'DELIM',
    'Comment',
    'Whitespace',
    'Block',
    'Statement',
    'Ruleset',
    'Parentheses',
    'Brackets',
    'Function'
)

instance = None

class CSSQC:
    def __init__(self, rules):
        self.events = {}
        for e in EVENTS:
            self.events[e] = []
        self.addRules(rules)
        self.parser = cssyacc.parser
        self.warnings = []
        instance = self
    
    def addRules(self, rules):
        for rule in rules:
            module = importlib.import_module("cssqc."+rule)
            klass = getattr(module, rule)
            self.addRuleObject(klass())
    
    def eventName(self, e):
        return "on_"+e
    
    def addRuleObject(self, o):
        for e in EVENTS:
            f = getattr(o, self.eventName(e), None)
            if callable(f):
                self.events[e].append((f,o))
    
    def event(self, e, data):
        for pair in self.events[e]:
            pair[0](pair[1], data)
    
    def parse(self, data):
        l = csslex.getLexer()
        result = self.parser.parse(data, lexer=l)
        return result

class QualityWarning:
    def __init__(self, rule, line):
        self.rule = rule
        self.line = line

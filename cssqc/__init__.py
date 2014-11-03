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
        global instance
        self.events = {}
        for e in EVENTS:
            self.events[e] = []
        self.addRules(rules)
        self.parser = cssyacc.parser
        self.warnings = []
        self.tokens = []
        self.current_token = 0
        instance = self
    
    def addRules(self, rules):
        for rule in rules:
            if rules[rule]:
                module = importlib.import_module("cssqc."+rule)
                klass = getattr(module, rule)
                self.addRuleObject(klass(rules[rule]))
    
    def eventName(self, e):
        return "on_"+e
    
    def addRuleObject(self, o):
        for e in EVENTS:
            f = getattr(o, self.eventName(e), None)
            if callable(f):
                self.events[e].append(f)
    
    def event(self, e, obj):
        for f in self.events[e]:
            self.warnings += f(obj)
    
    def token(self):
        if len(self.tokens) > self.current_token:
            t = self.tokens[self.current_token]
            self.current_token += 1
            return t
        else:
            return None
    
    def parse(self, data):
        l = csslex.getLexer()
        l.input(data)
        for token in l:
            self.tokens.append(token)
            self.event(token.type, token)
        result = self.parser.parse(lexer=self)
        return result

class QualityWarning:
    def __init__(self, rule, line, msg = ''):
        self.rule = rule
        self.line = line
        self.message = msg
    
    def __repr__(self):
        return '<QualityWarning rule="'+self.rule+'" line="'+str(self.line) + '">'
        
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.rule == other.rule \
            and self.line == other.line

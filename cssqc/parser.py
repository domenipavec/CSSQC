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

from cssyacc.ruleset import Ruleset

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
    'Block',
    'Brackets',
    'Comment',
    'Function',
    'Parentheses',
    'Ruleset',
    'Selector',
    'Statement',
    'Whitespace'
)

instance = None

class CSSQC:
    def __init__(self, rules):
        global instance
        self.events = {}
        for e in EVENTS:
            self.events[e] = []
        self.afterParse = []
        self.addRules(rules)
        self.parser = cssyacc.parser
        self.warnings = []
        self.tokens = []
        self.objects = []
        self.current_token = 0
        instance = self
    
    @staticmethod
    def getInstance():
        global instance
        return instance
    
    def addRules(self, rules):
        for rule in rules:
            try:
                enabled = rules.getboolean(rule)
            except:
                enabled = True
            if enabled:
                module = importlib.import_module("cssqc.rules."+rule)
                klass = getattr(module, rule)
                self.addRuleObject(klass(rules[rule]))
    
    def eventName(self, e):
        return "on_"+e
    
    def addRuleObject(self, o):
        for e in EVENTS:
            f = getattr(o, self.eventName(e), None)
            if callable(f):
                self.events[e].append(f)
        f = getattr(o, "afterParse", None)
        if callable(f):
            self.afterParse.append(f)
    
    def event(self, e, obj):
        for f in self.events[e]:
            self.warnings += f(obj)
    
    def register(self, name, obj):
        self.objects.append((name, obj))
    
    def token(self):
        if len(self.tokens) > self.current_token:
            t = self.tokens[self.current_token]
            self.current_token += 1
            return t
        else:
            return None
    
    def parse(self, data):
        # lex
        l = csslex.getLexer()
        l.input(data)
        
        # parse tokens
        for token in l:
            self.tokens.append(token)
            self.event(token.type, token)
        
        # yacc
        result = self.parser.parse(lexer=self)
        
        for el in result:
            if type(el) is Ruleset:
                el.setDepth(0)
        
        # parse objects
        for obj in self.objects:
            self.event(obj[0], obj[1])
            
        # after parse
        for f in self.afterParse:
            self.warnings += f(result)

        # sort warnings
        self.warnings.sort(key=lambda qw: qw.line)

        return result

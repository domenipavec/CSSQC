#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssyacc/block.py
# 
# class for block
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssyacc.statement import Statement
from cssyacc.ruleset import Ruleset
import cssqc.parser

class Block:
    def __init__(self, el, t, ln1, ln2):
        self.elements = el
        self.lb_lineno = ln1
        self.rb_lineno = ln2
        self.last = Statement(t, ln2)
        
        self.statements = 0
        self.blocks = 0
        for e in self.elements:
            if type(e) is Statement:
                self.statements += 1
            elif type(e) is Ruleset:
                self.blocks += 1
        if len(self.last.text) > 0:
            self.statements += 1
        
        i = cssqc.parser.CSSQC.getInstance()
        if i is not None:
            i.register(self.__class__.__name__, self)
    
    def isOneLiner(self):
        return self.statements <= 1 and self.blocks == 0
    
    def __str__(self):
        return ''.join(map(str, self.elements))
    
    def __len__(self):
        return len(self.elements)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.elements == other.elements\
            and self.last == other.last \
            and self.lb_lineno == other.lb_lineno \
            and self.rb_lineno == other.rb_lineno

    def __repr__(self):
        return '<Block>\n    ' + '\n    '.join(map(repr, self.elements)) + '\n</Block>'
        

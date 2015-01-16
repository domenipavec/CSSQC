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
from cssyacc.comment import Comment
from cssyacc.whitespace import Whitespace

class Block:
    def __init__(self, el, t, ln1, ln2):
        import cssqc.parser
        
        self.elements = el
        self.lb_lineno = ln1
        self.rb_lineno = ln2
        
        if t is not None \
            and len(t) > 0:
            
            # remove trailing ws and comments from t
            # make t a statement and append everything
            following = []
            while type(t[-1]) is Whitespace \
                or type(t[-1]) is Comment:
                following.append(t.pop())
            self.elements.append(Statement(t, ln2, False))
            self.elements += following
        
        self.statements = 0
        self.blocks = 0
        for e in self.elements:
            if type(e) is Statement:
                self.statements += 1
            elif type(e) is Ruleset:
                self.blocks += 1
        
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
            and self.lb_lineno == other.lb_lineno \
            and self.rb_lineno == other.rb_lineno

    def __repr__(self):
        return '<Block>\n    ' + '\n    '.join(map(repr, self.elements)) + '\n</Block>'

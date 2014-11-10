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
import cssqc

class Block:
    def __init__(self, el, t, ln1, ln2):
        self.elements = el
        self.lb_lineno = ln1
        self.rb_lineno = ln2
        self.last = Statement(t, ln2)
        
        if cssqc.instance is not None:
            cssqc.instance.event('Block', self)
    
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
        

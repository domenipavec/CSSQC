#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssyacc/statement.py
# 
# class for statement
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import cssqc.parser

class Statement:
    def __init__(self, t, ln, sc=True):
        self.lineno = ln
        self.semicolon = sc
        if t is None:
            self.text = []
        else:
            self.text = t

        if len(self.text) == 0:
            raise Exception('Empty statement on line %d.' % self.lineno)

        i = cssqc.parser.CSSQC.getInstance()
        if i is not None:
            i.register(self.__class__.__name__, self)
    
    def __str__(self):
        return ''.join(map(str, self.text))
    
    def __len__(self):
        return len(self.text)
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.text == other.text \
            and self.lineno == other.lineno \
            and self.semicolon == other.semicolon
  
    def __repr__(self):
        return '<Statement>\n    ' + '\n    '.join(map(repr, self.text)) + '\n</Statement>'
        

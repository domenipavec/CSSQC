#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssyacc/brackets.py
# 
# class for brackets
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import cssqc.parser

class Selector:
    def __init__(self, t, ln):
        self.lineno = ln
        if t is None:
            self.text = []
        else:
            self.text = t
        
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
            and self.lineno == other.lineno

    def __repr__(self):
        return '<Selector>\n    ' + '\n    '.join(map(repr, self.text)) + '\n</Selector>'

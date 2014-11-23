#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssyacc/function.py
# 
# class for function
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import cssqc.parser

class Function:
    def __init__(self, n, t, ln1, ln2):
        self.name_lineno = ln1
        self.rp_lineno = ln2
        if n is None:
            self.name = []
        else:
            self.name = n
        
        if t is None:
            self.text = []
        else:
            self.text = t
        
        i = cssqc.parser.CSSQC.getInstance()
        if i is not None:
            i.register(self.__class__.__name__, self)
    
    def __str__(self):
        return ''.join(map(str, self.name)) + ''.join(map(str, self.text)) + ')'
    
    def __len__(self):
        return len(self.text)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.text == other.text \
            and self.name == other.name \
            and self.name_lineno == other.name_lineno \
            and self.rp_lineno == other.rp_lineno

    def __repr__(self):
        return '<Function>\n    <Name>        \n' \
            + '\n        '.join(map(repr, self.name)) \
            + '\n    </Name>\n    <Text>' + '\n        '.join(map(repr, self.text)) + '\n    </Text>\n</Function>'
        

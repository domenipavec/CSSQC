#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssyacc/parentheses.py
# 
# class for parentheses
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

class Parentheses:
    def __init__(self, t, ln1, ln2):
        import cssqc.parser
        
        self.lp_lineno = ln1
        self.rp_lineno = ln2
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
            and self.lp_lineno == other.lp_lineno \
            and self.rp_lineno == other.rp_lineno


    def __repr__(self):
        return '<Parentheses>\n    ' + '\n    '.join(map(repr, self.text)) + '\n</Parentheses>'
        

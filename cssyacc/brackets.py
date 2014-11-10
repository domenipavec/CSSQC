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

import cssqc

class Brackets:
    def __init__(self, t, ln1, ln2):
        self.lb_lineno = ln1
        self.rb_lineno = ln2
        if t is None:
            self.text = []
        else:
            self.text = t
        
        if cssqc.instance is not None:
            cssqc.instance.event('Brackets', self)
    
    def __str__(self):
        return ''.join(map(str, self.text))
    
    def __len__(self):
        return len(self.text)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.text == other.text \
            and self.lb_lineno == other.lb_lineno \
            and self.rb_lineno == other.rb_lineno

    def __repr__(self):
        return '<Brackets>\n    ' + '\n    '.join(map(repr, self.text)) + '\n</Brackets>'
        

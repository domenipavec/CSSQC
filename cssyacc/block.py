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

class Block:
    def __init__(self, el, t):
        self.text = el
        if t is None:
            self.last = []
        else:
            self.last = t
    
    def __str__(self):
        return ''.join(map(str, self.text))
    
    def __len__(self):
        return len(self.text)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.text == other.text and self.last == other.last

    def __repr__(self):
        return '<Block>\n    ' + '\n    '.join(map(repr, self.text)) + '\n</Block>'
        
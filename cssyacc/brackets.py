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

class Brackets:
    def __init__(self, t):
        if t is None:
            self.text = []
        else:
            self.text = t
    
    def __str__(self):
        return ''.join(map(str, self.text))
    
    def __len__(self):
        return len(self.text)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.text == other.text

    def __repr__(self):
        return '<Brackets>\n    ' + '\n    '.join(map(repr, self.text)) + '\n</Brackets>'
        
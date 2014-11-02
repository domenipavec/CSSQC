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

class Function:
    def __init__(self, n, t):
        if n is None:
            self.name = []
        else:
            self.name = n
        
        if t is None:
            self.text = []
        else:
            self.text = t
    
    def __str__(self):
        return ''.join(map(str, self.name)) + ''.join(map(str, text)) + ')'
    
    def __len__(self):
        return len(self.text)
    
    def __repr__(self):
        return '<Function>\n    <Name>        \n' \
            + '\n        '.join(map(repr, self.name)) \
            + '\n    </Name>\n    <Text>' + '\n        '.join(map(repr, self.text)) + '\n    </Text>\n</Function>'
        
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

class Statement:
    def __init__(self, t):
        if t is None:
            self.text = []
        else:
            self.text = t
    
    def __str__(self):
        return ''.join(self.text)
    
    def __len__(self):
        return len(self.text)
    
    def __repr__(self):
        return '<Statement>\n    ' + '\n    '.join(map(repr, self.text)) + '\n</Statement>'
        
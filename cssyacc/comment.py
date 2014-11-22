#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssyacc/comment.py
# 
# class for comment
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import cssqc.parser

class Comment:
    def __init__(self, v, ln):
        self.value = v
        self.lineno = ln
        
        i = cssqc.parser.CSSQC.getInstance()
        if i is not None:
            i.event(self.__class__.__name__, self)
    
    def __str__(self):
        return self.value
    
    def __len__(self):
        return len(self.value)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.value == other.value \
            and self.lineno == other.lineno

    def __repr__(self):
        return '<Comment>\n' + self.value + '\n</Comment>'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssyacc/whitespace.py
# 
# class for whitespace
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import cssqc

class Whitespace:
    def __init__(self, v, ln):
        self.lineno = ln
        if v is None:
            self.value = ''
        else:
            self.value = v
        if cssqc.instance is not None:
            cssqc.instance.event('Whitespace', self)
    
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
        if self.value == '':
            return '<Whitespace>'
        else:
            return '<Whitespace value="' + repr(self.value) + '">'

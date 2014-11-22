#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/__init__.py
# 
# css quality control
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

class QualityWarning:
    def __init__(self, rule, line, msg = ''):
        self.rule = rule
        self.line = line
        self.message = msg
    
    def getLine(self):
        return self.line
    
    def __repr__(self):
        return '<QualityWarning rule="'+self.rule+'" line="'+str(self.line) + '">'

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.rule == other.rule \
            and self.line == other.line

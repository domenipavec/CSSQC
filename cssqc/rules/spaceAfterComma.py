#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/spaceAfterComma.py
# 
# Commas in lists should be followed by space.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssqc.helpers import isTupleWithValue, isLast
from cssyacc import Whitespace

def getHelp():
    return """Commas in lists should be followed by space."""

class spaceAfterComma:
    def __init__(self, data):
        self.on_Function = self.on_Parentheses

    def on_Parentheses(self, p):
        warnings = []
        for i in range(len(p.text)):
            if isTupleWithValue(p.text[i], ',') \
                and not (not isLast(i, p.text) \
                    and type(p.text[i+1]) is Whitespace \
                    and p.text[i+1].value == ' '):
                warnings.append(QualityWarning('spaceAfterComma', p.text[i][1], \
                    'Comma should be followed by space.'))
        return warnings
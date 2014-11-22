#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noUniversalSelectors.py
# 
# Do not allow universal selectors on their own.
# (e.g. div * {} is not allowed, but *.class {} is ok)
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace
from cssqc.helpers import isTupleWithValue, isLast

def getHelp():
    return """Do not allow universal selectors on their own (e.g. div * {} is not allowed, but *.class {} is ok)."""

class noUniversalSelectors:
    def __init__(self, data):
        pass

    def firstInSelectorOrDescendant(self, i, l):
        return i == 0 \
            or type(l[i-1]) is Whitespace
    
    def lastInSelectorOrHasDescendant(self, i, l):
        return isLast(i, l) \
            or type(l[i+1]) is Whitespace

    def on_Selector(self, s):
        warnings = []
        for i in range(len(s.text)):
            if isTupleWithValue(s.text[i], '*') \
                and self.firstInSelectorOrDescendant(i, s.text) \
                and self.lastInSelectorOrHasDescendant(i, s.text):
                warnings.append(QualityWarning('noUniversalSelectors', s.text[i][1], 'Universal selector present.'))
        return warnings

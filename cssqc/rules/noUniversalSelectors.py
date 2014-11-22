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
            or type(l[i-1]) is Whitespace \
            or isTupleWithValue(l[i-1], ',')
    
    def lastInSelectorOrHasDescendant(self, i, l):
        return isLast(i, l) \
            or type(l[i+1]) is Whitespace \
            or isTupleWithValue(l[i+1], ',')

    def on_Ruleset(self, rs):
        warnings = []
        for i in range(len(rs.name)):
            if isTupleWithValue(rs.name[i], '*') \
                and self.firstInSelectorOrDescendant(i, rs.name) \
                and self.lastInSelectorOrHasDescendant(i, rs.name):
                warnings.append(QualityWarning('noUniversalSelectors', rs.name[i][1], 'Universal selector present.'))
        return warnings

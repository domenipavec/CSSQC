#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noRedundantBodySelectors.py
# 
# Do not allow redundant body selectors.
# (e.g. body {} is ok, but body div {} is not)
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace
from cssqc.helpers import isTupleWithValues, isLast, isTupleWithValue

def getHelp():
    return """Do not allow redundant body selectors (e.g. body {} is ok, but body div {} is not)."""

class noRedundantBodySelectors:
    def __init__(self, data):
        pass

    def lastInRuleOrHasChild(self, i, l):
        return isLast(i, l) \
            or isTupleWithValue(l[i+1], '>') \
            or (type(l[i+1]) is Whitespace \
                and (isLast(i+1, l)
                    or isTupleWithValue(l[i+2], '>')))

    def on_Selector(self, s):
        warnings = []
        for i in range(len(s.text)):
            if isTupleWithValue(s.text[i], 'body') \
                and not self.lastInRuleOrHasChild(i, s.text):
                    warnings.append(QualityWarning('noRedundantBodySelectors', s.text[i][1], 'Redundant body selector.'))
        return warnings

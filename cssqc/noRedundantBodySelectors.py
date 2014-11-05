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

from cssqc import QualityWarning
from cssyacc import Whitespace
from cssqc.helpers import isTupleWithValues, isLast, isTupleWithValue

class noRedundantBodySelectors:
    def __init__(self, data):
        pass

    def lastInRuleOrHasChild(self, i, l):
        return isLast(i, l) \
            or isTupleWithValues(l[i+1], (',', '>')) \
            or (type(l[i+1]) is Whitespace \
                and (isLast(i+1, l)
                    or isTupleWithValues(l[i+2], (',', '>'))))

    def on_Ruleset(self, rs):
        warnings = []
        for i in range(len(rs.name)):
            if isTupleWithValue(rs.name[i], 'body') \
                and not self.lastInRuleOrHasChild(i, rs.name):
                    warnings.append(QualityWarning('noRedundantBodySelectors', rs.name[i][1], 'Redundant body selector.'))
        return warnings

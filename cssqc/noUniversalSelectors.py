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

from cssqc import QualityWarning
from cssyacc import Whitespace
from cssqc.helpers import isTupleWithValue, isLast

class noUniversalSelectors:
    def __init__(self, data):
        pass

    def on_Ruleset(self, rs):
        warnings = []
        for i in range(len(rs.name)):
            if isTupleWithValue(rs.name[i], '*') \
                and (i == 0 \
                    or type(rs.name[i-1]) is Whitespace \
                    or isTupleWithValue(rs.name[i-1], ',')) \
                and (isLast(i, rs.name) \
                    or type(rs.name[i+1]) is Whitespace \
                    or isTupleWithValue(rs.name[i+1], ',')):
                warnings.append(QualityWarning('noUniversalSelectors', rs.name[i][1], 'Universal selector present.'))
        return warnings

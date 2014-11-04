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

class noRedundantBodySelectors:
    def __init__(self, data):
        pass

    def on_Ruleset(self, rs):
        warnings = []
        for i in range(len(rs.name)):
            if type(rs.name[i]) is tuple:
                if rs.name[i][0][0:4] == 'body' and not \
                    (i == len(rs.name) - 1 or \
                    (type(rs.name[i+1]) is tuple and \
                        (rs.name[i+1][0] == ',' or \
                        rs.name[i+1][0] == '>')) or \
                    (type(rs.name[i+1]) is Whitespace and \
                        (i == len(rs.name) - 2 or \
                        (type(rs.name[i+2]) is tuple and \
                            (rs.name[i+2][0] == ',' or \
                            rs.name[i+2][0] == '>'))))):
                    warnings.append(QualityWarning('noRedundantBodySelectors', rs.name[i][1], 'Universal selector present.'))
        return warnings

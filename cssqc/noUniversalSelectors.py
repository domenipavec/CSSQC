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

class noUniversalSelectors:
    def __init__(self, data):
        pass

    def on_Ruleset(self, rs):
        warnings = []
        for i in range(len(rs.name)):
            if type(rs.name[i]) is tuple:
                if rs.name[i][0] == '*' \
                    and (i == 0 \
                        or type(rs.name[i-1]) is Whitespace \
                        or (type(rs.name[i-1]) is tuple and rs.name[i-1][0] == ',')) \
                    and (i == (len(rs.name) - 1) \
                        or type(rs.name[i+1]) is Whitespace \
                        or (type(rs.name[i+1]) is tuple and rs.name[i+1][0] == ',')):
                    warnings.append(QualityWarning('noUniversalSelectors', rs.name[i][1], 'Universal selector present.'))
        return warnings

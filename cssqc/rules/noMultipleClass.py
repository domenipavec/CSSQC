#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noMultipleClass.py
# 
# Do not allow multiple class (e.g. .class1.class2)
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from csslex import t_IDENT
from cssyacc import Whitespace, Comment
from cssqc.helpers import isTupleWithValue

import re

class noMultipleClass:
    def __init__(self, data):
        self.ident_re = re.compile(t_IDENT)

    def on_Ruleset(self, rs):
        warnings = []
        for i in range(len(rs.name)):
            try:
                class1 = rs.name[i+1][0]
                class2 = rs.name[i+3][0]
                if isTupleWithValue(rs.name[i], '.') \
                    and isTupleWithValue(rs.name[i+2], '.') \
                    and self.ident_re.match(class1) \
                    and self.ident_re.match(class2) \
                    and (i == 0 \
                        or type(rs.name[i-1]) is Whitespace \
                        or isTupleWithValue(rs.name[i-1], ',')):
                    warnings.append(QualityWarning('noMultipleClass', rs.name[i][1], 'Multiple classes: .' + class1 + '.' + class2))
            except:
                pass
        return warnings

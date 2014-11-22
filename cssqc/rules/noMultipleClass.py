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

def getHelp():
    return """Do not allow multiple class (e.g. .class1.class2)."""

class noMultipleClass:
    def __init__(self, data):
        self.ident_re = re.compile(t_IDENT)

    def on_Selector(self, s):
        warnings = []
        for i in range(len(s.text)):
            try:
                class1 = s.text[i+1][0]
                class2 = s.text[i+3][0]
                if isTupleWithValue(s.text[i], '.') \
                    and isTupleWithValue(s.text[i+2], '.') \
                    and self.ident_re.match(class1) \
                    and self.ident_re.match(class2) \
                    and (i == 0 \
                        or type(s.text[i-1]) is Whitespace):
                    warnings.append(QualityWarning('noMultipleClass', s.text[i][1], 'Multiple classes: .' + class1 + '.' + class2))
            except Exception as inst:
                pass
        return warnings

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/singleSelectorPerLine.py
# 
# Only allow one selector on each line.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace, Statement, Ruleset

import re

def getHelp():
    return """Only allow one selector on each line."""

class singleSelectorPerLine:
    def __init__(self, data):
        pass

    def on_Ruleset(self, rs):
        warnings = []
        for i in range(1, len(rs.selectors)):
            firstElement = rs.selectors[i].text[0]
            if not (type(firstElement) is Whitespace \
                and '\n' in firstElement.value):
                warnings.append(QualityWarning('singleSelectorPerLine', rs.selectors[i].lineno, \
                    'No new line before this selector.'))
        return warnings
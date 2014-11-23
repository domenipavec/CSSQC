#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/singlePropertyPerLine.py
# 
# Only allow one property on each line.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace, Statement, Ruleset

import re

def getHelp():
    return """Only allow one property on each line."""

class singlePropertyPerLine:
    def __init__(self, data):
        pass

    def on_Ruleset(self, rs):
        nl = True
        warnings = []
        for el in rs.block.elements:
            if type(el) is Whitespace \
                and '\n' in el.value:
                nl = True
            elif type(el) is Statement:
                if not nl:
                    warnings.append(QualityWarning('singlePropertyPerLine', el.lineno, \
                        'No new line before this statement.'))
                nl = False
            elif type(el) is Ruleset:
                if not nl:
                    warnings.append(QualityWarning('singlePropertyPerLine', el.block.lb_lineno, \
                        'No new line before this ruleset.'))
                nl = False
        if len(rs.block.last.text) > 0 \
            and not nl:
            warnings.append(QualityWarning('singlePropertyPerLine', rs.block.rb_lineno, \
                'No new line before last statement.'))
        return warnings
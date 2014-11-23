#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/onePropertySingleLine.py
# 
# Force single line format for rulesets with only one property.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace
from cssqc.helpers import inspectWhitespaces

import re

def getHelp():
    return """Force single line for rulesets with only one property."""

class onePropertySingleLine:
    def __init__(self, data):
        pass

    def on_Ruleset(self, rs):
        if rs.block.isOneLiner():
            if not inspectWhitespaces(rs.block, lambda ws: '\n' not in ws.value):
                return [QualityWarning('onePropertySingleLine', rs.block.lb_lineno, \
'Rulesets with only one property must be in single line.')]
        return []
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/selectorDepth.py
# 
# Allow only nested rules up to n-th level.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace, Comment, Parentheses
from cssqc.helpers import isTupleWithValues

import re

def getHelp():
    return """Allow selector depth up to 'n'. OPT must be integer."""

class selectorDepth:
    def __init__(self, data):
        self.maxDepth = int(data)

    def on_Selector(self, s):
        depth = -1
        att = False
        for el in s.text:
            if type(el) is Whitespace \
                or isTupleWithValues(el, ('+', '>')) \
                or type(el) is Comment \
                or type(el) is Parentheses:
                att = False
            elif not att:
                depth += 1
                att = True

        if depth > self.maxDepth:
            return [QualityWarning('selectorDepth', s.lineno, 'Selector depth longer than %d.' % self.maxDepth)]
        else:
            return []
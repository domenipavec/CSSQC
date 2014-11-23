#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/nestingDepth.py
# 
# Allow only nested rules up to n-th level.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from csslex import t_IDENT
from cssyacc import Whitespace
from cssqc.helpers import isTupleWithValue, isLast

import re

def getHelp():
    return """Allow only nested rules up to 'n'-th level. OPT must be integer."""

class nestingDepth:
    def __init__(self, data):
        self.maxDepth = int(data)

    def on_Ruleset(self, rs):
        if rs.depth > self.maxDepth:
            return [QualityWarning('nestingDepth', rs.block.lb_lineno, 'Block nested too deep.')]
        else:
            return []

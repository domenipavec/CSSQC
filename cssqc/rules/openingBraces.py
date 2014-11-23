#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/openingBraces.py
# 
# Opening braces on the same line preceeded by one space.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace

import re

def getHelp():
    return """Opening braces on the same line as last selector preceeded by one space, followed by newline (or space for oneliners)."""

class openingBraces:
    def __init__(self, data):
        pass

    def on_Ruleset(self, rs):
        lastSelector = rs.selectors[-1]
        preceedingElement = lastSelector.text[-1]
        if not (type(preceedingElement) is Whitespace \
            and preceedingElement.value == ' '):
            return [QualityWarning('openingBraces', rs.block.lb_lineno, \
'''Opening braces must be on the same line as last selector preceeded by one space.''')]
        
        firstElement = None
        if len(rs.block.elements) > 0:
            firstElement = rs.block.elements[0]
        elif len(rs.block.last.text) > 0:
            firstElement = rs.block.last.text[0]
        if not (firstElement is not None \
            and type(firstElement) is Whitespace \
            and ((rs.block.isOneLiner() \
                    and firstElement.value == ' ')
                or firstElement.value[0] == '\n')):
            return [QualityWarning('openingBraces', rs.block.lb_lineno, \
'''Opening braces must be followed by newline or space for oneliners.''')]
        
        return []
            
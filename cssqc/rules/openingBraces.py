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
from cssqc.helpers import isSpacesOnly

import re

def getHelp():
    return """Opening braces on the same line as last selector preceeded by one space, followed by newline (or space for oneliners).
Options are 'exact' and 'atleast'. 'atleast' allows any number of spaces."""

class openingBraces:
    def __init__(self, data):
        if data == "exact":
            self.exact = True
        elif data == 'atleast':
            self.exact = False
        else:
            raise Exception('Invalid input for rule openingBraces.')

    def on_Ruleset(self, rs):
        lastSelector = rs.selectors[-1]
        preceedingElement = lastSelector.text[-1]
        if not (type(preceedingElement) is Whitespace \
            and ((self.exact and preceedingElement.value == ' ') \
                 or (not self.exact and isSpacesOnly(preceedingElement.value)))):
            return [QualityWarning('openingBraces', rs.block.lb_lineno, \
'''Opening braces must be on the same line as last selector preceeded by one space.''')]
        
        firstElement = None
        if len(rs.block.elements) > 0:
            firstElement = rs.block.elements[0]
        if not (type(firstElement) is Whitespace \
            and ((rs.block.isOneLiner() \
                    and ((self.exact and firstElement.value == ' ') \
                         or (not self.exact and isSpacesOnly(firstElement.value)))) \
                or firstElement.value[0] == '\n')):
            return [QualityWarning('openingBraces', rs.block.lb_lineno, \
'''Opening braces must be followed by newline or space for oneliners.''')]
        
        return []
            
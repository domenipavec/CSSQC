#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/closingBraces.py
# 
# Closing braces on its own line.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace
from cssqc.helpers import isSpacesOnly

import re

def getHelp():
    return """Closing braces on its own line, for oneliners preceeded by space.
Options are 'exact' and 'atleast'. 'atleast' allows any number of spaces."""

class closingBraces:
    def __init__(self, data):
        if data == "exact":
            self.exact = True
        elif data == 'atleast':
            self.exact = False
        else:
            raise Exception('Invalid input for rule openingBraces.')

    def on_Ruleset(self, rs):
        lastElement = None
        if len(rs.block.elements) > 0:
            lastElement = rs.block.elements[-1]
        
        if not (lastElement is not None \
            and type(lastElement) is Whitespace \
            and ((rs.block.isOneLiner() \
                    and ((self.exact and lastElement.value == ' ') \
                         or (not self.exact and isSpacesOnly(lastElement.value)))) \
                or '\n' in lastElement.value)):
            return [QualityWarning('closingBraces', rs.block.rb_lineno, \
'Closing brace must be on its own line or preceeded by space for oneliners.')]
        
        return []
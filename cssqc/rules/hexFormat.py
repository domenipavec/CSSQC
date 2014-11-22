#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/hexFormat.py
# 
# Format hex colors.
# Options are 'long' (6character hex code only), 
# 'short' (use 3 character hex when possible),
# 'uppercase', 'lowercase', 
# and 'validate' (warning if not 3 or 6 character)
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssqc.helpers import isTupleWithValue
from bisect import bisect_left

def getHelp():
    return """Format hex colors. Options are 
'long' (must be 6 characters long)
'short' (must be 3 characters when possible)
'lowercase', 'uppercase' and
'validate' (must be 3 or 6 characters long)."""

class hexFormat:
    def __init__(self, data):
        self.on_Parentheses = self.on_Function
        if 'long' in data:
            self.check_long = True
        else:
            self.check_long = False
        if 'short' in data:
            self.check_short = True
        else:
            self.check_short = False
        if 'uppercase' in data:
            self.check_upper = True
        else:
            self.check_upper = False
        if 'lowercase' in data:
            self.check_lower = True
        else:
            self.check_lower = False
        if 'validate' in data:
            self.check_validate = True
        else:
            self.check_validate = False
        self.last_err = ""

    def isInvalidColor(self, v):
        vlower = v.lower()
        if v[0] == '#':
            if self.check_long and len(v) == 4:
                self.last_err = 'Hex "%s" is not long.' % v
                return True
            if self.check_short \
                and len(v) == 7 \
                and vlower[1] == vlower[2] \
                and vlower[3] == vlower[4] \
                and vlower[5] == vlower[6]:
                self.last_err = 'Hex "%s" should be short.' % v
                return True
            if self.check_lower \
                and (len(v) == 7 or len(v) == 4) \
                and vlower != v:
                self.last_err = 'Hex "%s" should be lowercase.' % v
                return True
            if self.check_upper \
                and (len(v) == 7 or len(v) == 4) \
                and v.upper() != v:
                self.last_err = 'Hex "%s" should be uppercase.' % v
                return True
            if self.check_validate \
                and not (len(v) == 7 or len(v) == 4):
                self.last_err = 'Hex "%s" invalid hex.' % v
                return True
        else:
            return False

    def on_Function(self, f):
        warnings = []
        for t in f.text:
            if type(t) is tuple \
                and self.isInvalidColor(t[0]):
                warnings.append(QualityWarning('hexFormat', t[1], self.last_err))
        return warnings
    
    def on_Statement(self, statement):
        warnings = []
        is_after_colon = False
        for t in statement.text:
            if is_after_colon:
                if type(t) is tuple \
                    and self.isInvalidColor(t[0]):
                    warnings.append(QualityWarning('hexFormat', t[1], self.last_err))
            else:
                if isTupleWithValue(t, ':'):
                    is_after_colon = True
        return warnings

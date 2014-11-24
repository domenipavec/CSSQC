#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/colonFormat.py
# 
# Format of spaces around colon(:) in properties.
# Options are 'before', 'after', 'both', 'none' and 'align'.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from csslex import t_IDENT
from cssyacc import Whitespace, Statement
from cssqc.helpers import isTupleWithValue, isLast

import re

def getHelp():
    return """Format of spaces around colon(:) in properties.
Options are 'before', 'after', 'both', 'none' and 'align'. You can specify multiple options separated by comma."""

class colonFormat:
    def __init__(self, data):
        options = data.split(',')
        self.opt_before = False
        self.opt_after = False
        self.opt_both = False
        self.opt_none = False
        self.opt_align = False
        for opt in options:
            if opt == 'before':
                self.opt_before = True
            elif opt == 'after':
                self.opt_after = True
            elif opt == 'both':
                self.opt_both = True
            elif opt == 'none':
                self.opt_none = True
            elif opt == 'align':
                self.opt_align = True
            else:
                raise Exception('Invalid input for rule colonFormat.')
        
        self.ws_before = None
        self.ws_after = None
        self.align_reset = True

    def isProperty(self, s):
        i = 0
        # property name
        if not (type(s.text[i]) is tuple \
                and len(s.text[i][0]) > 1) \
            or isLast(i, s.text):
            return False
        i += 1
        # optional ws
        if type(s.text[i]) is Whitespace:
            self.ws_before = s.text[i]
            if isLast(i, s.text):
                return False
            i += 1
        else:
            self.ws_before = None
        # colon
        if not isTupleWithValue(s.text[i], ':') \
            or isLast(i, s.text):
            return False
        i += 1
        # optional ws
        if type(s.text[i]) is Whitespace:
            self.ws_after = s.text[i]
            if isLast(i, s.text):
                return False
            i += 1
        else:
            self.ws_after = None
        # value
        if not type(s.text[i]) is tuple:
            return False
        else:
            return True

    def colonFormatBefore(self):
        return self.ws_after is None \
            and self.ws_before is not None \
            and self.ws_before.value == ' '
    
    def colonFormatAfter(self):
        return self.ws_before is None \
            and self.ws_after is not None \
            and self.ws_after.value == ' '
    
    def colonFormatBoth(self):
        return self.ws_before is not None \
            and self.ws_before.value == ' ' \
            and self.ws_after is not None \
            and self.ws_after.value == ' '
    
    def colonFormatNone(self):
        return self.ws_before is None \
            and self.ws_after is None

    def colonFormatAlign(self, s):
        if self.align_reset:
            self.align_reset = False
            
            if not(self.ws_before is not None \
                and self.ws_after is not None \
                and self.ws_after.value == ' '):
                return False
            
            for x in self.ws_before.value:
                if x != ' ':
                    return False
            
            self.align_length = len(s.text[0][0]) + len(self.ws_before.value)
            
            self.align_init = True
            
            return True
        elif self.align_init:
            if not(self.ws_before is not None \
                and self.ws_after is not None \
                and self.ws_after.value == ' '):
                return False
            
            for x in self.ws_before.value:
                if x != ' ':
                    return False
                
            if len(s.text[0][0]) + len(self.ws_before.value) == self.align_length:
                return True
            else:
                return False
        else:
            return False

    def on_Ruleset(self, rs):
        warnings = []
        self.align_reset = True
        self.align_init = False
        for el in rs.block.elements:
            if type(el) is Statement \
                and self.isProperty(el):
                if self.opt_align and self.colonFormatAlign(el):
                    continue
                elif self.opt_after and self.colonFormatAfter():
                    continue
                elif self.opt_both and self.colonFormatBoth():
                    continue
                elif self.opt_none and self.colonFormatNone():
                    continue
                elif self.opt_before and self.colonFormatBefore():
                    continue
                else:
                    warnings.append(QualityWarning('colonFormat', el.lineno, \
                        'Wrong formatted colon in statement.'))
        
        return warnings
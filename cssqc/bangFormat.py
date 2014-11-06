#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/bangFormat.py
# 
# Format of spaces around ! before important.
# Options are 'before', 'after', 'both' and 'none'.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc import QualityWarning
from csslex import t_IDENT
from cssyacc import Whitespace
from cssqc.helpers import isTupleWithValue, isLast

import re

class bangFormat:
    def __init__(self, data):
        if data == 'before':
            self.bangFormat = self.bangFormatBefore
        elif data == 'after':
            self.bangFormat = self.bangFormatAfter
        elif data == 'both':
            self.bangFormat = self.bangFormatBoth
        elif data == 'none':
            self.bangFormat = self.bangFormatNone
        else:
            raise Exception('Invalid input for rule noOverqualifying.')

    def bangFormatBefore(self, i, l):
        return type(l[i-1]) is Whitespace \
            and not isLast(i, l) \
            and isTupleWithValue(l[i+1], 'important')
    
    def bangFormatAfter(self, i, l):
        return type(l[i-1]) is not Whitespace \
            and not isLast(i, l) \
            and type(l[i+1]) is Whitespace \
            and l[i+1].value == ' ' \
            and not isLast(i+1, l) \
            and isTupleWithValue(l[i+2], 'important')
    
    def bangFormatBoth(self, i, l):
        return type(l[i-1]) is Whitespace \
            and not isLast(i, l) \
            and type(l[i+1]) is Whitespace \
            and l[i+1].value == ' ' \
            and not isLast(i+1, l) \
            and isTupleWithValue(l[i+2], 'important')
    
    def bangFormatNone(self, i, l):
        return type(l[i-1]) is not Whitespace \
            and not isLast(i, l) \
            and isTupleWithValue(l[i+1], 'important')

    def on_Statement(self, statement):
        for i in range(1, len(statement)):
            if isTupleWithValue(statement.text[i], '!'):
                if not self.bangFormat(i, statement.text):
                    return [QualityWarning('bangFormat', statement.text[i][1], 'Invalid bang format.')]
        return []

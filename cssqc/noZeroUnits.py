#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noZeroUnits.py
# 
# Do not allow units after 0 value.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc import QualityWarning
from csslex import ident, flags

import re

class noZeroUnits:
    def __init__(self, data):
        self.on_PERCENTAGE = self.on_DIMENSION
        self.regex = re.compile(flags + r'(0+|0*\.0+)(%|('+ident+r'))')

    def on_DIMENSION(self, i):
        if self.regex.match(i.value):
            return [QualityWarning('noZeroUnits', i.lineno, 'A zero with units appears: ' + i.value)]
        else:
            return []
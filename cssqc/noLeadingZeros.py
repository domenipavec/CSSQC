#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noLeadingZeros.py
# 
# Do not allow leading zeros with decimals (e.g. 0.3px).
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc import QualityWarning
from csslex import ident, flags

import re

class noLeadingZeros:
    def __init__(self, data):
        self.on_PERCENTAGE = self.on_DIMENSION
        self.on_NUMBER = self.on_DIMENSION
        self.leading_zeros_re = re.compile(flags + r'(0+\.[0-9]*)(%|('+ident+r'))?')

    def on_DIMENSION(self, i):
        if self.leading_zeros_re.match(i.value):
            return [QualityWarning('noLeadingZeros', i.lineno, 'A leading zero appears: ' + i.value)]
        else:
            return []

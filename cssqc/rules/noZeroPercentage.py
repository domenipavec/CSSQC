#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noZeroPercentage.py
# 
# Do not allow percentage after 0 value.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from csslex import ident, flags

import re

def getHelp():
    return """Do not allow percentage after 0 value."""

class noZeroPercentage:
    def __init__(self, data):
        self.zero_with_units_re = re.compile(flags + r'(0+|0*\.0+)(%)')

    def on_PERCENTAGE(self, i):
        if self.zero_with_units_re.match(i.value):
            return [QualityWarning('noZeroPercentage', i.lineno, 'A zero with percentage appears: ' + i.value)]
        else:
            return []

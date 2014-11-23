#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/singleLinePerProperty.py
# 
# Do not allow property on multiple lines.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace
from cssqc.helpers import inspectWhitespaces

import re

def getHelp():
    return """Do not allow property over multiple lines."""

class singleLinePerProperty:
    def __init__(self, data):
        pass

    def on_Statement(self, s):
        ln = inspectWhitespaces(s, lambda ws: '\n' not in ws.value)
        if ln != -1 \
            and not (type(s.text[-1]) is Whitespace \
                and s.text[-1].lineno == ln):
            return [QualityWarning('singleLinePerProperty', ln, 'Property over multiple lines.')]
        else:
            return []
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/finalNewline.py
# 
# File must have newline at the end.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace

class finalNewline:
    def __init__(self, data):
        pass

    def afterParse(self, result):
        if len(result) > 0 \
            and type(result[-1]) is Whitespace \
            and result[-1].value[-1] == '\n':
            return []
        else:
            return [QualityWarning('finalNewline', -1, 'File does not contain a new line at the end.')]

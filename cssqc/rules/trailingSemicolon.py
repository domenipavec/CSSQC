#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/trailingSemicolon.py
# 
# Last property in ruleset must have semicolon.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning

import re

def getHelp():
    return """Last property in ruleset must be semicolon terminated."""

class trailingSemicolon:
    def __init__(self, data):
        pass

    def on_Statement(self, s):
        if not s.semicolon:
            return [QualityWarning('trailingSemicolon', s.lineno, 'Should have semicolon at the end.')]
        else:
            return []
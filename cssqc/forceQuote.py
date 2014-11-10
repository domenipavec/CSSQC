#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/forceQuote.py
# 
# Force single or double quotes.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc import QualityWarning

class forceQuote:
    def __init__(self, data):
        self.doubleq = (data == "double")

    def on_STRING(self, i):
        if self.doubleq and i.value[0] == "'":
            return [QualityWarning('forceQuote', i.lineno, "Single quote used.")]
        elif not self.doubleq and i.value[0] == '"':
            return [QualityWarning('forceQuote', i.lineno, "Double quote used.")]
        else:
            return []

    def on_URI(self, i):
        if self.doubleq and "'" in i.value:
            return [QualityWarning('forceQuote', i.lineno, "Single quote used.")]
        elif not self.doubleq and '"' in i.value:
            return [QualityWarning('forceQuote', i.lineno, "Double quote used.")]
        else:
            return []

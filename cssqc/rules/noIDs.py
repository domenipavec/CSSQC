#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noIDs.py
# 
# Do not allow IDs in selectors.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning

def getHelp():
    return """Do not allow IDs in selectors."""

class noIDs:
    def __init__(self, data):
        pass

    def on_Selector(self, s):
        warnings = []
        for token in s.text:
            if type(token) is tuple:
                if token[0][0] == '#':
                    warnings.append(QualityWarning('noIDs', token[1], 'ID "%s" present.' % token[0]))
        return warnings

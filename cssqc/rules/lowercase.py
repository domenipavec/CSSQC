#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/lowercase.py
# 
# Force everything lowercase except hex colors.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning

def getHelp():
    return """Force everything lowercase except hex color, strings and comments."""

class lowercase:
    def __init__(self, data):
        self.on_ATKEYWORD = self.on_IDENT
        self.on_ATBRACES = self.on_IDENT
        self.on_DIMENSION = self.on_IDENT
        

    def on_IDENT(self, i):
        if i.value.lower() != i.value:
            return [QualityWarning('lowercase', i.lineno, '"%s" is not lowercase.' % i.value)]
        else:
            return []

    def on_URI(self, i):
        if i.value[:3] != "url":
            return [QualityWarning('lowercase', i.lineno, '"%s" is not lowercase.' % i.value)]
        else:
            return []

    def on_Ruleset(self, rs):
        warnings = []
        for e in rs.name:
            if type(e) is tuple \
                and e[0][0] == '#' \
                and e[0].lower() != e[0]:
                warnings.append(QualityWarning('lowercase', e[1], '"%s" is not lowercase.' % e[0]))
        return warnings

    def on_Statement(self, s):
        warnings = []
        for e in s.text:
            if type(e) is tuple:
                if e[0] == ':':
                    break
                elif e[0][0] == '#' \
                    and e[0].lower() != e[0]:
                    warnings.append(QualityWarning('lowercase', e[1], '"%s" is not lowercase.' % e[0]))
        return warnings

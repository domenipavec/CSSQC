#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/propertyValidate.py
# 
# Order properties.
# Orders are defined in cssqc/order/*.dat.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace, Statement
from cssqc.helpers import isProperty

from pkg_resources import resource_string

def getHelp():
    return """Validate property names."""

class propertyValidate:
    def __init__(self, data):
        self.properties = set()

        o = resource_string('cssqc', 'order/alphabetical.dat').decode('utf-8')
        for x in o.split('\n'):
            self.properties.add(x)

    def on_Statement(self, s):
        if isProperty(s):
            if s.text[0][0] in self.properties \
                or s.text[0][0][0] == '-' \
                or s.text[0][0][0] == '@':
                return []
            else:
                return [QualityWarning('propertyValidate', s.text[0][1], 'Invalid property.')]
        else:
            return []
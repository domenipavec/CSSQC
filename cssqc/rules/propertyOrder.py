#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/propertyOrder.py
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
    return """Force ordered properties.
Orders are defined in 'cssqc/order/*.dat'. OPT must be valid order name."""

class propertyOrder:
    def __init__(self, data):
        self.reverseIndex = {}
        i = 0
        o = resource_string('cssqc', 'order/' + data + '.dat').decode('utf-8')
        for x in o.split('\n'):
            self.reverseIndex[x] = i
            i += 1

    def on_Ruleset(self, rs):
        warnings = []
        last_index = -1
        for el in rs.block.elements:
            if type(el) is Statement \
                and isProperty(el):
                pname = el.text[0][0]
                if pname in self.reverseIndex:
                    if self.reverseIndex[pname] < last_index:
                        warnings.append(QualityWarning('propertyOrder', el.text[0][1], \
                            'Property in wrong place.'))
                    else:
                        last_index = self.reverseIndex[pname]
        return warnings
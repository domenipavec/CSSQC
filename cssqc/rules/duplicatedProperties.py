#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/duplicatedProperties.py
# 
# Warn on duplicated properties in ruleset.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace, Statement
from cssqc.helpers import isProperty

from pkg_resources import resource_string

def getHelp():
    return """Warn on duplicated properties in ruleset."""

class duplicatedProperties:
    def __init__(self, data):
        pass

    def on_Ruleset(self, rs):
        properties = set()
        warnings = []
        for el in rs.block.elements:
            if type(el) is Statement \
                and isProperty(el):
                if el.text[0][0] in properties:
                    warnings.append(QualityWarning('duplicatedProperties', el.text[0][1], \
                        'Duplicated property.'))
                else:
                    properties.add(el.text[0][0])
        return warnings
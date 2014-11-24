#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noDescendantSelector.py
# 
# Do not allow descendant selectors.
# (e.g. div > a {} is ok, but div a {} is not)
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace, Comment, Parentheses
from cssqc.helpers import isTupleWithValues

def getHelp():
    return """Do not allow descendant selectors."""

class noDescendantSelector:
    def __init__(self, data):
        pass

    def on_Selector(self, s):
        descendant = False
        att = False
        for el in s.text:
            if type(el) is Whitespace:
                att = False
            elif isTupleWithValues(el, ('+', '>')) \
                or type(el) is Comment \
                or type(el) is Parentheses:
                descendant = False
            elif not att:
                if descendant:
                    return [QualityWarning('noDescendantSelector', s.lineno, 'Descendant selector present.')]
                att = True
                descendant = True
        return []

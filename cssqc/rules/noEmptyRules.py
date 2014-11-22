#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noEmptyRules.py
# 
# Do not allow rules with empty blocks.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace, Comment

class noEmptyRules:
    def __init__(self, data):
        pass

    def on_Ruleset(self, rs):
        if len(rs.block.last) != 0:
            return []
        for element in rs.block.elements:
            if not (type(element) is Whitespace or type(element) is Comment):
                return []
        return [QualityWarning('noEmptyRules', rs.block.lb_lineno, 'Empty rule present.')]

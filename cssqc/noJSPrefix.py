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

from cssqc import QualityWarning

class noJSPrefix:
    def __init__(self):
        pass

    def on_IDENT(self, i):
        if i.value[0:3] == "js-":
            return [QualityWarning('noJSPrefix', i.lineno)]
        else:
            return []

    def on_HASH(self, i):
        if i.value[1:4] == "js-":
            return [QualityWarning('noJSPrefix', i.lineno)]
        else:
            return []

        

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noUnderscores.py
# 
# Do not underscores in class, id and mixin names.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc import QualityWarning

class noUnderscores:
    def __init__(self, data):
        self.on_HASH = self.on_IDENT
        self.on_ATKEYWORD = self.on_IDENT
        self.on_ATBRACES = self.on_IDENT
        self.on_FUNCTION = self.on_IDENT

    def on_IDENT(self, i):
        if '_' in i.value:
            return [QualityWarning('noUnderscores', i.lineno, 'Underscore appears in "%s".' % i.value)]
        else:
            return []

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/statistics.py
# 
# Count ids, tags, classes, selectors, ...
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssyacc import Whitespace
from cssqc.helpers import isLast, isTupleWithValue, isProperty

class Counter:
    def __init__(self):
        self.unique_set = set()
        self.unique = 0
        self.total = 0
    
    def pair(self):
        return (self.total, self.unique)
    
    def count(self, s):
        self.total += 1
        if s not in self.unique_set:
            self.unique += 1
            self.unique_set.add(s)

class Statistics:
    def __init__(self):
        self.ids = Counter()
        self.classes = Counter()
        self.tags = Counter()
        self.selectors = Counter()
        self.properties = Counter()

    def on_Selector(self, s):
        self.selectors.count(str(s))
        for i in range(len(s.text)):
            el = s.text[i]
            if type(el) is tuple:
                # ids
                if el[0][0] == '#':
                    self.ids.count(el[0])
                # classes
                elif el[0] == '.' \
                    and not isLast(i, s.text) \
                    and type(s.text[i+1]) is tuple:
                    self.classes.count(s.text[i+1][0])
                # tags
                elif len(el[0]) > 1 \
                    and i != 0 \
                    and not isTupleWithValue(s.text[i-1], '.'):
                    self.tags.count(el[0])
        return []
    
    def on_Statement(self, s):
        if isProperty(s):
            self.properties.count(s.text[0][0])
        return []
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_hexFormat.py
# 
# test for hexFormat rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_hexFormat(unittest.TestCase):
    def parse(self, data, l):
        c = CSSQC({"hexFormat": l})
        c.parse(data)
        return c

    def assertItemsEqual(self, l1, l2):
        self.assertEqual(sorted(l1, key=QualityWarning.getLine), sorted(l2, key=QualityWarning.getLine))

    def parseSample(self, l):
        sample = '''/* variables */
@c1: #f2f;
@c2: #F2F;
@c3: #f2F;
@c4: #FE23AB;
@c5: #ff23ff;
@c6: #FE22ff;
@c7: #ff22ff;
@c8: #f3;
@c9: #ff89b;
/* ids, colors and mixins */
#f2f {
    color: #f2f;
    #f2f;
}
#F2F {
    color: #F2F;
    #F2F;
}
#f2F {
    color: #f2F;
    #f2F;
}
#ff22ff {
    color: #ff22ff;
    #ff22ff;
}
#f2fe {
    color: #f2fe;
    #f2fe;
}
/* parameters */
.foo (@bg: #f2f) {
  background: @bg;
}
.foo (@bg: #F2F) {
  background: @bg;
}
.foo (@bg: #f2F) {
  background: @bg;
}
.foo (@bg: #ff22ff) {
  background: @bg;
}
.foo (@bg: #ff2ef) {
  background: @bg;
}'''
        warnings_dict = {
            'long': [
                QualityWarning('hexFormat', 2),
                QualityWarning('hexFormat', 3),
                QualityWarning('hexFormat', 4),
                QualityWarning('hexFormat', 13),
                QualityWarning('hexFormat', 17),
                QualityWarning('hexFormat', 21),
                QualityWarning('hexFormat', 33),
                QualityWarning('hexFormat', 36),
                QualityWarning('hexFormat', 39)
            ],
            'short': [
                QualityWarning('hexFormat', 8),
                QualityWarning('hexFormat', 25),
                QualityWarning('hexFormat', 42)
            ],
            'lowercase': [
                QualityWarning('hexFormat', 3),
                QualityWarning('hexFormat', 4),
                QualityWarning('hexFormat', 5),
                QualityWarning('hexFormat', 7),
                QualityWarning('hexFormat', 17),
                QualityWarning('hexFormat', 21),
                QualityWarning('hexFormat', 36),
                QualityWarning('hexFormat', 39)
            ],
            'uppercase': [
                QualityWarning('hexFormat', 2),
                QualityWarning('hexFormat', 4),
                QualityWarning('hexFormat', 6),
                QualityWarning('hexFormat', 7),
                QualityWarning('hexFormat', 8),
                QualityWarning('hexFormat', 13),
                QualityWarning('hexFormat', 21),
                QualityWarning('hexFormat', 25),
                QualityWarning('hexFormat', 33),
                QualityWarning('hexFormat', 39),
                QualityWarning('hexFormat', 42)
            ],
            'validate': [
                QualityWarning('hexFormat', 9),
                QualityWarning('hexFormat', 10),
                QualityWarning('hexFormat', 29),
                QualityWarning('hexFormat', 45)
            ]
        }
        c = self.parse(sample, l)
        warnings = []
        for i in l:
            for w in warnings_dict[i]:
                if w not in warnings:
                    warnings.append(w)
        self.assertItemsEqual(c.warnings, warnings)
    
    def test_nothing(self):
        self.parseSample([])
    
    def test_long(self):
        self.parseSample(['long'])
    
    def test_short(self):
        self.parseSample(['short'])
    
    def test_lowercase(self):
        self.parseSample(['lowercase'])
    
    def test_uppercase(self):
        self.parseSample(['uppercase'])
    
    def test_validate(self):
        self.parseSample(['validate'])

    def test_combinations(self):
        cs = (('long', 'short'), ('lowercase', 'uppercase'))
        for i in range(3):
            for j in range(3):
                for k in range(2):
                    l = []
                    if i < 2:
                        l.append(cs[0][i])
                    if j < 2:
                        l.append(cs[1][j])
                    if k < 1:
                        l.append('validate')
                    if len(l) > 1:
                        self.parseSample(l)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_selectorDepth.py
# 
# test for selectorDepth rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_selectorDepth(unittest.TestCase):
    def parse(self, data, i):
        c = CSSQC({"selectorDepth": str(i)})
        c.parse(data)
        return c

    
    def test_selector_depth(self):
        sample = '''div {
    margin: 0;
}
div .class1 {
    padding: 0;
}
span>.class1 > .class2 {
    color: blue;
}'''
        c0 = self.parse(sample, 0)
        c1 = self.parse(sample, 1)
        c2 = self.parse(sample, 2)
        c3 = self.parse(sample, 3)

        self.assertEqual(c3.warnings, [ ])
        self.assertEqual(c2.warnings, [ ])
        self.assertEqual(c1.warnings, [
            QualityWarning('selectorDepth', 7)
        ])
        self.assertEqual(c0.warnings, [
            QualityWarning('selectorDepth', 4),
            QualityWarning('selectorDepth', 7)
        ])

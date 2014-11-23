#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_nestingDepth.py
# 
# test for nestingDepth rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_nestingDepth(unittest.TestCase):
    def parse(self, data, i):
        c = CSSQC({"nestingDepth": str(i)})
        c.parse(data)
        return c

    
    def test_nesting_depth(self):
        sample = '''div {
    margin: 0;
}
div {
    .class1 {
        padding: 0;
    }
}
div {
    .class1 {
        .class2 {
            color: black;
        }
    }
}'''
        c0 = self.parse(sample, 0)
        c1 = self.parse(sample, 1)
        c2 = self.parse(sample, 2)
        c3 = self.parse(sample, 3)

        self.assertEqual(c3.warnings, [ ])
        self.assertEqual(c2.warnings, [ ])
        self.assertEqual(c1.warnings, [
            QualityWarning('nestingDepth', 11)
        ])
        self.assertEqual(c0.warnings, [
            QualityWarning('nestingDepth', 5),
            QualityWarning('nestingDepth', 10),
            QualityWarning('nestingDepth', 11)
        ])

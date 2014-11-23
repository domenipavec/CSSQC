#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_onePropertySingleLine.py
# 
# test for onePropertySingleLine rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_opnePropertySingleLine(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"onePropertySingleLine": "on"})
        c.parse(data)
        return c

    
    def test_one_property_single_line(self):
        sample = '''div { margin: 0; }
span {
    margin: 0;
}
.class1 {
    padding: 0; }
.class2 { margin: 0;
}
.class3 { padding:
            0; }'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('onePropertySingleLine', 2),
            QualityWarning('onePropertySingleLine', 5),
            QualityWarning('onePropertySingleLine', 7),
            QualityWarning('onePropertySingleLine', 9)
        ])


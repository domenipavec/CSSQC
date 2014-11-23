#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_singleSelectorPerLine.py
# 
# test for singleSelectorPerline rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_singleSelectorPerLine(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"singleSelectorPerLine": "on"})
        c.parse(data)
        return c

    
    def test_sspl(self):
        sample = '''div { margin: 0; }
span, div {
    padding: 0;
}
.class1,
.class2 {
    margin: 0;
}
.class3, .class4, .class5 {
    padding: 0;
}'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('singleSelectorPerLine', 2),
            QualityWarning('singleSelectorPerLine', 9),
            QualityWarning('singleSelectorPerLine', 9)
        ])


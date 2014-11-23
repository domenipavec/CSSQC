#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_singlePropertyPerLine.py
# 
# test for singlePropertyPerline rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_singlePropertyPerLine(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"singlePropertyPerLine": "on"})
        c.parse(data)
        return c

    
    def test_sppl(self):
        sample = '''div { margin: 0; padding 0; }
span {
    margin: 0;
    color: blue;
}
.class1 {
    padding: 0; margin: 0
}
.class2 {
    padding: 0
             0;
}
.class3 { padding: 0; }'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('singlePropertyPerLine', 1),
            QualityWarning('singlePropertyPerLine', 8)
        ])


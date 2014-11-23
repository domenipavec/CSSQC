#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_openingBraces.py
# 
# test for openingBraces rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_openingBraces(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"openingBraces": "on"})
        c.parse(data)
        return c

    
    def test_opening_braces(self):
        sample = '''div {
    margin: 0;
}
span{
    color: blue;
}
.class1
{
    color: #fff;
}
.class2 { margin: 0; }
.class3 { margin: 0; padding: 0 }'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('openingBraces', 4),
            QualityWarning('openingBraces', 8),
            QualityWarning('openingBraces', 12)
        ])


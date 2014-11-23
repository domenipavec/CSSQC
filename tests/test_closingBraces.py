#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_closingBraces.py
# 
# test for closingBraces rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_closingBraces(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"closingBraces": "on"})
        c.parse(data)
        return c

    
    def test_closing_braces(self):
        sample = '''div {
    margin: 0;
}
span {
    margin: 0;
    color: blue; }
.class1 {
    padding: 0;
    color: #fff;}
.class2 {
    margin: 0;
    color: #fff }
.class3 {
    margin: 0;
    padding: 0}
.class4 {
    height: 100%;
}
.class5 { margin: 0; }'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('closingBraces', 6),
            QualityWarning('closingBraces', 9),
            QualityWarning('closingBraces', 12),
            QualityWarning('closingBraces', 15)
        ])


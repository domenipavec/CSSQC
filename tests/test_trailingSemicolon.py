#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_trailingSemicolon.py
# 
# test for trailingSemicolon rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_trailingSemicolon(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"trailingSemicolon": "on"})
        c.parse(data)
        return c

    
    def test_trailing_semicolon(self):
        sample = '''div {
    margin: 0;
    padding: 0;
}
span {
    margin: 0;
    padding: 0
}
.class1 { color: blue; }
.class2 { color: red }'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('trailingSemicolon', 8),
            QualityWarning('trailingSemicolon', 10)
        ])


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_singleLinePerProperty.py
# 
# test for singleLinePerProperty rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_singleLinePerProperty(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"singleLinePerProperty": "on"})
        c.parse(data)
        return c

    
    def test_slpp(self):
        sample = '''span {
    margin: 0;
    color: blue;
    padding: 0
}
.class1 {
    padding: 0; margin: 0
}
.class2 {
    padding: 0
             0;
}
.class3 { padding: 0; }
.class4 {
    margin : 0
    0
}'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('singleLinePerProperty', 10),
            QualityWarning('singleLinePerProperty', 15)
        ])


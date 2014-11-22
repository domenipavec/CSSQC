#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_lowercase.py
# 
# test for lowercase rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_lowercase(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"lowercase": True})
        c.parse(data)
        return c
        
    def assertItemsEqual(self, l1, l2):
        self.assertEqual(sorted(l1, key=QualityWarning.getLine), sorted(l2, key=QualityWarning.getLine))
    
    def test_lowercase(self):
        c = self.parse('''/* Comment does not matter */
body {
    margin: 0
}
.claSs {
    Padding: 0;
}
#iD {
    color: #FFdfe2;
    #mixIn();
}
.foo (@bg: #FF22ff) {
  background: @bg;
}''')
        self.assertItemsEqual(c.warnings, [
            QualityWarning('lowercase', 5),
            QualityWarning('lowercase', 6),
            QualityWarning('lowercase', 8),
            QualityWarning('lowercase', 10)
        ])

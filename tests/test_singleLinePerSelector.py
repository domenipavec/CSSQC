#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_singleLinePerSelector.py
# 
# test for singleLinePerSelector rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_singleLinePerSelector(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"singleLinePerSelector": "on"})
        c.parse(data)
        return c

    
    def test_slps(self):
        sample = '''span .class1 {
    color: blue;
}
.class1, .class2
{
    padding: 0;
}

.class2
.class3 {
    padding: 0;
}
'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('singleLinePerSelector', 9)
        ])


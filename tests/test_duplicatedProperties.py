#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_duplicatedProperties.py
# 
# test for duplicatedProperties rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_duplicatedProperties(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"duplicatedProperties": "on"})
        c.parse(data)
        return c

    
    def test_duplicates(self):
        sample = '''div {
    color: blue;
    border: 0;
    color: red;
}
span {
    border: 1px;
}
'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('duplicatedProperties', 4)
        ])


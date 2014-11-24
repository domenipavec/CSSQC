#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_propertyOrder.py
# 
# test for propertyOrder rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_propertyOrder(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"propertyOrder": "alphabetical"})
        c.parse(data)
        return c

    
    def test_property_order(self):
        sample = '''div {
    color: blue;
    border: 0;
    margin: 0;
    padding: 0;
    height: 0;
    left: 0;
    width: 0;
}
'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('propertyOrder', 3),
            QualityWarning('propertyOrder', 6),
            QualityWarning('propertyOrder', 7)
        ])


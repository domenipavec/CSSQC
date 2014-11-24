#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_propertyValidate.py
# 
# test for propertyValidate rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_propertyValidate(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"propertyValidate": "on"})
        c.parse(data)
        return c

    
    def test_property_validate(self):
        sample = '''div {
    color: blue;
    borderr: 0;
    -webkit-background-clip: padding;
}
@color : #fff;
'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('propertyValidate', 3)
        ])


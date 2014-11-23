#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noZeroPercentage.py
# 
# test for noZeroPercentage rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_noZeroPercentage(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noZeroPercentage": True})
        c.parse(data)
        return c
    
    def test_no_zero_units(self):
        c = self.parse('''div {
    height: 0;
    width: 0%;
    margin-top: 0px;
    margin-bottom: 0em;
    margin-left: .0em;
    margin-right: .0%;
    padding-top: 0.0px;
    padding-right: 0.000em;
    padding-left: .00px;
    padding-bottom: .0;
}''')
        self.assertEqual(c.warnings, [
            QualityWarning('noZeroPercentage', 3),
            QualityWarning('noZeroPercentage', 7)
        ])

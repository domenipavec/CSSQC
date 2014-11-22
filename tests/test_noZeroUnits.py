#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noZeroUnits.py
# 
# test for noZeroUnits rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_noZeroUnits(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noZeroUnits": True})
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
            QualityWarning('noZeroUnits', 3),
            QualityWarning('noZeroUnits', 4),
            QualityWarning('noZeroUnits', 5),
            QualityWarning('noZeroUnits', 6),
            QualityWarning('noZeroUnits', 7),
            QualityWarning('noZeroUnits', 8),
            QualityWarning('noZeroUnits', 9),
            QualityWarning('noZeroUnits', 10),
        ])

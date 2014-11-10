#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noTrailingZeros.py
# 
# test for noTrailingZeros rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc import CSSQC, QualityWarning

class Test_noTrailingZeros(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noTrailingZeros": True})
        c.parse(data)
        return c
    
    def test_no_trailing_zeros(self):
        c = self.parse('''div {
    height: 0.10px;
    width: 0.2%;
    margin-top: 0px;
    margin-bottom: 10em;
    margin-left: .0em;
    margin-right: 0.1%;
    padding-top: 00.3px;
    padding-right: 00.3;
    padding-left: .00px;
    padding-bottom: .0;
}''')
        self.assertEqual(c.warnings, [
            QualityWarning('noTrailingZeros', 2),
            QualityWarning('noTrailingZeros', 6),
            QualityWarning('noTrailingZeros', 10),
            QualityWarning('noTrailingZeros', 11)
        ])

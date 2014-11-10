#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noLeadingZeros.py
# 
# test for noLeadingZeros rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc import CSSQC, QualityWarning

class Test_noLeadingZeros(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noLeadingZeros": True})
        c.parse(data)
        return c
    
    def test_no_leading_zeros(self):
        c = self.parse('''div {
    height: 0.1px;
    width: 0.2%;
    margin-top: 0px;
    margin-bottom: 10.0em;
    margin-left: .0em;
    margin-right: .0%;
    padding-top: 00.3px;
    padding-right: 00.3;
    padding-left: .00px;
    padding-bottom: .0;
}''')
        self.assertEqual(c.warnings, [
            QualityWarning('noLeadingZeros', 2),
            QualityWarning('noLeadingZeros', 3),
            QualityWarning('noLeadingZeros', 8),
            QualityWarning('noLeadingZeros', 9)
        ])

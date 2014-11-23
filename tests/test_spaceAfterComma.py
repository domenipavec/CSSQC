#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_spaceAfterComma.py
# 
# test for spaceAfterComma rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_spaceAfterComma(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"spaceAfterComma": "on"})
        c.parse(data)
        return c

    
    def test_sac(self):
        sample = '''@include box-shadow(0 2px 2px rgba(0,0,0,.2));
color: rgba(0,0,0,.1);
@include box-shadow(0 2px 2px rgba(0, 0, 0, .2));
color: rgba(0, 0, 0, .1);'''

        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('spaceAfterComma', 1),
            QualityWarning('spaceAfterComma', 1),
            QualityWarning('spaceAfterComma', 1),
            QualityWarning('spaceAfterComma', 2),
            QualityWarning('spaceAfterComma', 2),
            QualityWarning('spaceAfterComma', 2)
        ])


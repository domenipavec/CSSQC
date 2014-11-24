#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_groupProperties.py
# 
# test for groupProperties rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_groupProperties(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"groupProperties": "galjot"})
        c.parse(data)
        return c

    
    def test_group_pr(self):
        sample = '''div {
    position: relative;
    z-index: 6;
    margin: 0;
    
    padding: 0;
    width: 100px;
    height: 60px;
    
    border: 0;
    /* background & color */
    background: #fff;
    color: #333;
    text-align: center
}
'''
        c = self.parse(sample)

        self.assertEqual(c.warnings, [
            QualityWarning('groupProperties', 4),
            QualityWarning('groupProperties', 14)
        ])


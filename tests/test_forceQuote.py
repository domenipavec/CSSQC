#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_forceQuote.py
# 
# test for forceQuote rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_forceQuote(unittest.TestCase):
    def setUp(self):
        self.sample = '''a:after {
    content: " ";
}
a:before {
    content: ' ';
}
div {
    background: url("image.png");
}
div.class1 {
    bakcground: url('image.png');
}'''
    
    def parseSingle(self):
        c = CSSQC({"forceQuote": "single"})
        c.parse(self.sample)
        return c
    
    def parseDouble(self):
        c = CSSQC({"forceQuote": "double"})
        c.parse(self.sample)
        return c
    
    def test_single_quote(self):
        c = self.parseSingle()
        self.assertEqual(c.warnings, [
            QualityWarning('forceQuote', 2),
            QualityWarning('forceQuote', 8)
        ])
    
    def test_double_quote(self):
        c = self.parseDouble()
        self.assertEqual(c.warnings, [
            QualityWarning('forceQuote', 5),
            QualityWarning('forceQuote', 11)
        ])

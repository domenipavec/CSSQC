#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_bangFormat.py
# 
# test for bangFormat rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_bangFormat(unittest.TestCase):
    def parseBefore(self, data):
        c = CSSQC({"bangFormat": 'before'})
        c.parse(data)
        return c
    
    def parseAfter(self, data):
        c = CSSQC({"bangFormat": 'after'})
        c.parse(data)
        return c

    def parseBoth(self, data):
        c = CSSQC({"bangFormat": 'both'})
        c.parse(data)
        return c
    
    def parseNone(self, data):
        c = CSSQC({"bangFormat": 'none'})
        c.parse(data)
        return c
    
    def test_bang_format(self):
        sample = '''div {
    width: 100% !important;
}
.class1 {
    height: 100% ! important;
}
.class2 {
    width: 50%!important;
}
.class3 {
    margin: 0! important;
}'''
        c_before = self.parseBefore(sample)
        c_after = self.parseAfter(sample)
        c_both = self.parseBoth(sample)
        c_none = self.parseNone(sample)
        self.assertEqual(c_before.warnings, [
            QualityWarning('bangFormat', 5),
            QualityWarning('bangFormat', 8),
            QualityWarning('bangFormat', 11)
        ])
        self.assertEqual(c_after.warnings, [
            QualityWarning('bangFormat', 2),
            QualityWarning('bangFormat', 5),
            QualityWarning('bangFormat', 8),
        ])
        self.assertEqual(c_both.warnings, [
            QualityWarning('bangFormat', 2),
            QualityWarning('bangFormat', 8),
            QualityWarning('bangFormat', 11),
        ])
        self.assertEqual(c_none.warnings, [
            QualityWarning('bangFormat', 2),
            QualityWarning('bangFormat', 5),
            QualityWarning('bangFormat', 11),
        ])

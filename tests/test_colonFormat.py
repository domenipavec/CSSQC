#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_colonFormat.py
# 
# test for colonFormat rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_colonFormat(unittest.TestCase):
    def setUp(self):
        self.sample = '''div {
    width: 100%;
}
.class1 {
    height : 100%;
}
.class2 {
    width :50%;
}
.class3 {
    margin:0;
}
.class4 {
    -webkit-border-image : @url @iwidth repeat;
    -moz-border-image    : @url @iwidth repeat;
    border-image         : @url @iwidth repeat;
    border-width         : @bwidth;
    background-clip      : padding-box;
    border-style        : solid;
}'''
    
    def parseBefore(self, data):
        c = CSSQC({"colonFormat": 'before'})
        c.parse(data)
        return c
    
    def parseAfter(self, data):
        c = CSSQC({"colonFormat": 'after'})
        c.parse(data)
        return c

    def parseBoth(self, data):
        c = CSSQC({"colonFormat": 'both'})
        c.parse(data)
        return c
    
    def parseNone(self, data):
        c = CSSQC({"colonFormat": 'none'})
        c.parse(data)
        return c
    
    def parseAlign(self, data):
        c = CSSQC({"colonFormat": 'align'})
        c.parse(data)
        return c
    
    def test_cf_before(self):
        c_before = self.parseBefore(self.sample)
        self.assertEqual(c_before.warnings, [
            QualityWarning('colonFormat', 2),
            QualityWarning('colonFormat', 5),
            QualityWarning('colonFormat', 11),
            QualityWarning('colonFormat', 14),
            QualityWarning('colonFormat', 15),
            QualityWarning('colonFormat', 16),
            QualityWarning('colonFormat', 17),
            QualityWarning('colonFormat', 18),
            QualityWarning('colonFormat', 19)
        ])
    
    def test_cf_after(self):
        c_after = self.parseAfter(self.sample)
        self.assertEqual(c_after.warnings, [
            QualityWarning('colonFormat', 5),
            QualityWarning('colonFormat', 8),
            QualityWarning('colonFormat', 11),
            QualityWarning('colonFormat', 14),
            QualityWarning('colonFormat', 15),
            QualityWarning('colonFormat', 16),
            QualityWarning('colonFormat', 17),
            QualityWarning('colonFormat', 18),
            QualityWarning('colonFormat', 19)
        ])
    
    def test_cf_both(self):
        c_both = self.parseBoth(self.sample)
        self.assertEqual(c_both.warnings, [
            QualityWarning('colonFormat', 2),
            QualityWarning('colonFormat', 8),
            QualityWarning('colonFormat', 11),
            QualityWarning('colonFormat', 15),
            QualityWarning('colonFormat', 16),
            QualityWarning('colonFormat', 17),
            QualityWarning('colonFormat', 18),
            QualityWarning('colonFormat', 19)
        ])
    
    def test_cf_none(self):
        c_none = self.parseNone(self.sample)
        self.assertEqual(c_none.warnings, [
            QualityWarning('colonFormat', 2),
            QualityWarning('colonFormat', 5),
            QualityWarning('colonFormat', 8),
            QualityWarning('colonFormat', 14),
            QualityWarning('colonFormat', 15),
            QualityWarning('colonFormat', 16),
            QualityWarning('colonFormat', 17),
            QualityWarning('colonFormat', 18),
            QualityWarning('colonFormat', 19)
        ])
        
    def test_cf_align(self):
        c_align = self.parseAlign(self.sample)
        self.assertEqual(c_align.warnings, [
            QualityWarning('colonFormat', 2),
            QualityWarning('colonFormat', 8),
            QualityWarning('colonFormat', 11),
            QualityWarning('colonFormat', 19)
        ])

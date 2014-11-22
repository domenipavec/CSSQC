#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noOverqualifying.py
# 
# test for noOverqualifying rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_noOverqualifying(unittest.TestCase):
    def parseClass(self, data):
        c = CSSQC({"noOverqualifying": 'class'})
        c.parse(data)
        return c
    
    def parseID(self, data):
        c = CSSQC({"noOverqualifying": 'id'})
        c.parse(data)
        return c

    def parseBoth(self, data):
        c = CSSQC({"noOverqualifying": 'both'})
        c.parse(data)
        return c

    def assertItemsEqual(self, l1, l2):
        self.assertEqual(sorted(l1, key=QualityWarning.getLine), sorted(l2, key=QualityWarning.getLine))
    
    def test_id_class(self):
        sample = '''#id1.class1 {
    margin: 0;
}
.class2#id2 {
    margin: 0;
}
body .class3#id3 {
    margin: 0;
}'''
        c_class = self.parseClass(sample)
        c_id = self.parseID(sample)
        c_both = self.parseBoth(sample)
        self.assertItemsEqual(c_class.warnings, [])
        self.assertItemsEqual(c_id.warnings, [
            QualityWarning('noOverqualifying', 1),
            QualityWarning('noOverqualifying', 4),
            QualityWarning('noOverqualifying', 7)
        ])
        self.assertItemsEqual(c_both.warnings, [
            QualityWarning('noOverqualifying', 1),
            QualityWarning('noOverqualifying', 4),
            QualityWarning('noOverqualifying', 7)
        ])

    def test_id_nested(self):
        sample = '''span #id1 {
    color: blue;
}
span .class1 {
    color: blue;
}
.class2 #id2 {
    color: red;
}'''
        c_class = self.parseClass(sample)
        c_id = self.parseID(sample)
        c_both = self.parseBoth(sample)
        self.assertItemsEqual(c_class.warnings, [])
        self.assertItemsEqual(c_id.warnings, [
            QualityWarning('noOverqualifying', 1),
            QualityWarning('noOverqualifying', 7)
        ])
        self.assertItemsEqual(c_both.warnings, [
            QualityWarning('noOverqualifying', 1),
            QualityWarning('noOverqualifying', 7)
        ])
    
    def test_id_tag(self):
        sample = '''#id1 {
    margin: 0;
}
div#id2 {
    margin: 0;
}
body div#id3.class1 {
    margin: 0;
}'''
        c_class = self.parseClass(sample)
        c_id = self.parseID(sample)
        c_both = self.parseBoth(sample)
        self.assertItemsEqual(c_class.warnings, [])
        self.assertItemsEqual(c_id.warnings, [
            QualityWarning('noOverqualifying', 4),
            QualityWarning('noOverqualifying', 7)
        ])
        self.assertItemsEqual(c_both.warnings, [
            QualityWarning('noOverqualifying', 4),
            QualityWarning('noOverqualifying', 7)
        ])

    def test_class_tag(self):
        sample = '''div.class1 {
    margin: 0;
}
div.class2 {
    padding: 0;
}
span.class2 {
    margin: 0;
}
div.class3, span.class3 {
    margin: 0;
}
div.class4 {
    margin: 0;
}
body, span.class4 {
    padding: 0;
}
div.class5 {
    margin: 0;
}
div.class5 {
    padding: 0;
}'''
        c_class = self.parseClass(sample)
        c_id = self.parseID(sample)
        c_both = self.parseBoth(sample)
        self.assertItemsEqual(c_class.warnings, [
            QualityWarning('noOverqualifying', 1),
            QualityWarning('noOverqualifying', 19)
        ])
        self.assertItemsEqual(c_id.warnings, [])
        self.assertItemsEqual(c_both.warnings, [
            QualityWarning('noOverqualifying', 1),
            QualityWarning('noOverqualifying', 19)
        ])
    
    def test_both(self):
        sample = '''#id1 {
    margin: 0;
}
div#id2 {
    margin: 0;
}
div.class1 {
    margin: 0;
}'''
        c_class = self.parseClass(sample)
        c_id = self.parseID(sample)
        c_both = self.parseBoth(sample)
        self.assertItemsEqual(c_class.warnings, [
            QualityWarning('noOverqualifying', 7)
        ])
        self.assertItemsEqual(c_id.warnings, [
            QualityWarning('noOverqualifying', 4)
        ])
        self.assertItemsEqual(c_both.warnings, [
            QualityWarning('noOverqualifying', 4),
            QualityWarning('noOverqualifying', 7)
        ])

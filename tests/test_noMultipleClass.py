#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noMultipleClass.py
# 
# test for noMultipleClass rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc import CSSQC, QualityWarning

class Test_noMultipleClass(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noMultipleClass": True})
        c.parse(data)
        return c
    
    def test_no_multiple_class(self):
        sample = '''#id1.class1 {
    margin: 0;
}
div.class2 {
    margin: 0;
}
body .class4.class3 {
    margin: 0;
}
body,.class5.class4{
    padding: 0;
}
.class5.class6 {
    width: 100%;
}
.class7.class3.class8 {
    height: 50px;
}'''
        c = self.parse(sample)
        self.assertEqual(c.warnings, [
            QualityWarning('noMultipleClass', 7),
            QualityWarning('noMultipleClass', 10),
            QualityWarning('noMultipleClass', 13),
            QualityWarning('noMultipleClass', 16)
        ])

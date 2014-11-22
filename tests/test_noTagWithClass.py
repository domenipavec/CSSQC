#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noTagWithClass.py
# 
# test for noTagWithClass rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_noTagWithClass(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noTagWithClass": True})
        c.parse(data)
        return c
    
    def test_no_tag_with_class(self):
        sample = '''#id1.class1 {
    margin: 0;
}
div.class2 {
    margin: 0;
}
body div.class3 {
    margin: 0;
}
body,
div.class4{
    padding: 0;
}
.class5 {
    width: 100%;
}'''
        c = self.parse(sample)
        self.assertEqual(c.warnings, [
            QualityWarning('noTagWithClass', 4),
            QualityWarning('noTagWithClass', 7),
            QualityWarning('noTagWithClass', 11)
        ])

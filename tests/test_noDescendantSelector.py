#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noDescendantSelector.py
# 
# test for noDescendantSelector rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_noDescendantSelector(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noDescendantSelector": "on"})
        c.parse(data)
        return c
    
    def test_no_descendant_selector(self):
        c = self.parse('''body {
    margin: 0;
}
.class1 h2 {
    margin: 0;
}
ul li a {
    color: blue;
}
body > h1 {
    padding: 0;
}
.module1>body > h2 {
    padding: 3px;
}''')
        self.assertEqual(c.warnings, [
            QualityWarning('noDescendantSelector', 4),
            QualityWarning('noDescendantSelector', 7)
        ])

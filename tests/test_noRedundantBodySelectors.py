#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noRedundantBodySelectors.py
# 
# test for noRedundantBodySelectors rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc import CSSQC, QualityWarning

class Test_noRedundantBodySelectors(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noRedundantBodySelectors": True})
        c.parse(data)
        return c
    
    def test_no_universal_selectors(self):
        c = self.parse('''body {
    margin: 0;
}
.module body h2 {
    margin: 0;
}
body ul li a {
    color: blue;
}
body > h1 {
    padding: 0;
}
.module1 body > h2 {
    padding: 3px;
}
.modal-popup-mode body {
    overflow: hidden;
}
.model-popup-mode body a {
    color: red;
}
body,
body h2,body .class1,
body > h1 {
    padding: 0;
}
body{
    height: 100%;
}''')
        self.assertEqual(c.warnings, [
            QualityWarning('noRedundantBodySelectors', 4),
            QualityWarning('noRedundantBodySelectors', 7),
            QualityWarning('noRedundantBodySelectors', 19),
            QualityWarning('noRedundantBodySelectors', 23),
            QualityWarning('noRedundantBodySelectors', 23)
        ])

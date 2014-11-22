#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noColorKeyword.py
# 
# test for noColorKeyword rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_noColorKeyword(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noColorKeyword": True})
        c.parse(data)
        return c
    
    def test_no_color_keyword(self):
        c = self.parse('''// Variables
@link-color:        Blue;
@link-color-hover:  darken(@link-color, 10%);

// Usage
a,
.link {
  color: @link-color;
}
a:hover {
  color: @link-color-hover;
}
.widget {
  color: black;
  background: @link-color;
}
.black {
    color: #000;
    .black; // mixin
    #black; // mixin 2
}
.foo (@bg: #f5f5f5, @color: blue) {
  background: @bg;
  color: @color;
}
.foo1(@bg: #f5f5f5, @color: blue) {
  background: @bg;
  color: @color;
}''')
        self.assertEqual(c.warnings, [
            QualityWarning('noColorKeyword', 2),
            QualityWarning('noColorKeyword', 14),
            QualityWarning('noColorKeyword', 22),
            QualityWarning('noColorKeyword', 26)
        ])

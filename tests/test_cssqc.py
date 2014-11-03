#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_cssqc.py
# 
# test for quality control
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc import CSSQC, QualityWarning

class Test_noIDs(unittest.TestCase):
    def parse(self, data):
        c = CSSQC(["noIDs"])
        c.parse(data)
        return c
    
    def test_without_ids(self):
        c = self.parse('''// Variables
@link-color:        #428bca; // sea blue
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
  color: #fff;
  background: @link-color;
}''')
        self.assertEqual(c.warnings, [])
    
    def test_with_ids(self):
        c = self.parse('''body #e5id {
    color: red;
}
a:hover {
    color: blue;
}
#trinity{}''')
        self.assertEqual(c.warnings, [QualityWarning('noIDs', 1), QualityWarning('noIDs', 7)])
    
    def test_color_arguments(self):
        c = self.parse('''.foo (@bg: #f5f5f5, @color: #900) {
  background: @bg;
  color: @color;
}
.unimportant {
  .foo();
}
.important {
  .foo() !important;
}''')
        self.assertEqual(c.warnings, [])
    
    def test_mixed_id_tag_class(self):
        c = self.parse('''div#id1 { }
#id1.cl1 { }
div#id1.cl1 { }''')
        self.assertEqual(c.warnings, [
            QualityWarning('noIDs', 1),
            QualityWarning('noIDs', 2),
            QualityWarning('noIDs', 3)
        ])


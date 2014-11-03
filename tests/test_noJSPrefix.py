#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noJSPrefix.py
# 
# test for noJSPrefix rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc import CSSQC, QualityWarning

class Test_noJSPrefix(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noJSPrefix": True})
        c.parse(data)
        return c
    
    def test_without_jsprefix(self):
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
    
    def test_with_jsprefix(self):
        c = self.parse('''body .js-class {
    color: red;
}
a:hover {
    color: blue;
}
#js-id{}''')
        self.assertEqual(c.warnings, [QualityWarning('noJSPrefix', 1), QualityWarning('noJSPrefix', 7)])
    
    def test_mixed_id_tag_class(self):
        c = self.parse('''div#js-id1 { }
#id1.js-class { }
div#id1.js-class { }''')
        self.assertEqual(c.warnings, [
            QualityWarning('noJSPrefix', 1),
            QualityWarning('noJSPrefix', 2),
            QualityWarning('noJSPrefix', 3)
        ])


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noEmptyRules.py
# 
# test for noEmptyRules rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc import CSSQC, QualityWarning

class Test_noEmptyRules(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noEmptyRules": True})
        c.parse(data)
        return c
    
    def test_no_empty_rules(self):
        c = self.parse('''body {}
h2 {
    margin: 0;
}
div {
    
}
span {
    // this is empty span
}
.class1 {
    .class2 {
        padding: 0;
    }
}
h1 {
    margin: 0
}
''')
        self.assertEqual(c.warnings, [
            QualityWarning('noEmptyRules', 1),
            QualityWarning('noEmptyRules', 5),
            QualityWarning('noEmptyRules', 8)
        ])

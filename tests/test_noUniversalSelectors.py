#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noUniversalSelectors.py
# 
# test for noUniversalSelectors rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc import CSSQC, QualityWarning

class Test_noUniversalSelectors(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noUniversalSelectors": True})
        c.parse(data)
        return c
    
    def test_no_universal_selectors(self):
        c = self.parse('''* {
    margin: 0;
}
div * {
}
*.class {
  color: blue;
}
*{
    padding: none;
}
span *{
    width: 100px;
},
table *, div {
    display: none;
}
span,* {
    padding: 5px;
}''')
        self.assertEqual(c.warnings, [
            QualityWarning('noUniversalSelectors', 1),
            QualityWarning('noUniversalSelectors', 4),
            QualityWarning('noUniversalSelectors', 9),
            QualityWarning('noUniversalSelectors', 12),
            QualityWarning('noUniversalSelectors', 15),
            QualityWarning('noUniversalSelectors', 18)
        ])

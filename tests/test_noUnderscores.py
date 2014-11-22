#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noUnderscores.py
# 
# test for noUnderscores rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_noUnderscores(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noUnderscores": True})
        c.parse(data)
        return c
    
    def test_no_underscores(self):
        c = self.parse('''.class_name {
    margin: auto;
}
#id_name {
    padding: 0;
}
@nice_blue: #5b83AD;
.@{my_selector} {
    margin: 0;
}
.my_mixin() {
    background: white;
}
.my-mixin2() {
    background: black;
}''')
        self.assertEqual(c.warnings, [
            QualityWarning('noUnderscores', 1),
            QualityWarning('noUnderscores', 4),
            QualityWarning('noUnderscores', 7),
            QualityWarning('noUnderscores', 8),
            QualityWarning('noUnderscores', 11)
        ])

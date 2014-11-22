#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_finalNewline.py
# 
# test for finalNewline rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_finalNewline(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"finalNewline": True})
        c.parse(data)
        return c
    
    def test_no_final_newline(self):
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
            QualityWarning('finalNewline', -1)
        ])
        
        c = self.parse('''body {
} ''')
        self.assertEqual(c.warnings, [
            QualityWarning('finalNewline', -1)
        ])
        
        c = self.parse('''body {
}
// comment''')
        self.assertEqual(c.warnings, [
            QualityWarning('finalNewline', -1)
        ])

        c = self.parse('''body {
}
@color: #ff0000;''')
        self.assertEqual(c.warnings, [
            QualityWarning('finalNewline', -1)
        ])

    def test_final_newline(self):
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
}
''')
        self.assertEqual(c.warnings, [])

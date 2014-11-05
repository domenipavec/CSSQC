#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_noRedundantChildSelectors.py
# 
# test for noRedundantChildSelectors rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc import CSSQC, QualityWarning

class Test_noRedundantChildSelectors(unittest.TestCase):
    def parse(self, data):
        c = CSSQC({"noRedundantChildSelectors": True})
        c.parse(data)
        return c
    
    def redundancy_parent_child(self, p, c):
        c = self.parse('''.class1 > %(parent)s %(child)s {
    margin: 0;
}
%(parent)s %(child)s {
    margin: 0;
}
%(parent)s.class2 %(child)s {
    padding: 0;
}
%(parent)s %(child)s > a {
    color: red;
}
div %(parent)s > %(child)s {
    padding: 0;
}
.class3 > %(parent)s > %(child)s > a {
    color: blue
}''' % {'parent': p, 'child': c})
        self.assertEqual(c.warnings, [
            QualityWarning('noRedundantChildSelectors', 4),
            QualityWarning('noRedundantChildSelectors', 10),
            QualityWarning('noRedundantChildSelectors', 13)
        ])
    
    def test_no_redundant_table_th(self):
        self.redundancy_parent_child('table', 'th')
    
    def test_no_redundant_table_td(self):
        self.redundancy_parent_child('table', 'td')
    
    def test_no_redundant_table_tr(self):
        self.redundancy_parent_child('table', 'tr')
    
    def test_no_redundant_ol(self):
        self.redundancy_parent_child('ol', 'li')
    
    def test_no_redundant_ul(self):
        self.redundancy_parent_child('ul', 'li')
    
    def test_no_redundant_select(self):
        self.redundancy_parent_child('select', 'option')

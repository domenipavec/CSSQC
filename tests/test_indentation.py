#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_indentation.py
# 
# test for indentation rule
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
from cssqc.parser import CSSQC
from cssqc.qualityWarning import QualityWarning

class Test_indentation(unittest.TestCase):

    def parse_indentation(self, c, i):
        c.parse('''div,
 span {{
{0}margin: 0;
   padding: 0;
{0}{0}color: blue;
   
{0}.class1,  
   .class2,
{0}{0}.class3 {{

{0}{0}top: 0;
   bottom: 0;
{0}{0}{0}width: 100%;

{0}}}
}}
@c1: #fff;
 @c2: #bbb;
.border-box {{
{0}-webkit-box-sizing: border-box;
{0}   -moz-box-sizing: border-box;
{0}        box-sizing: border-box;
}}
.class4 {{
{0}margin: 0
}}
.class5 {{
{0}padding: 0
   }}'''.format(i))
        self.assertEqual(c.warnings, [
            QualityWarning('indentation', 2),
            QualityWarning('indentation', 4),
            QualityWarning('indentation', 5),
            QualityWarning('indentation', 8),
            QualityWarning('indentation', 9),
            QualityWarning('indentation', 12),
            QualityWarning('indentation', 13),
            QualityWarning('indentation', 18),
            QualityWarning('indentation', 29)
        ])
    
    def test_tab(self):
        c = CSSQC({"indentation": "tab"})
        self.parse_indentation(c, '\t')
    
    def test_4spaces(self):
        c = CSSQC({"indentation": "4"})
        self.parse_indentation(c, '    ')

    def test_2spaces(self):
        c = CSSQC({"indentation": "2"})
        self.parse_indentation(c, '  ')

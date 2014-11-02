#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_csslex.py
# 
# test for tokenizer
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
import pprint
import cssyacc
import csslex

class TestCssyacc(unittest.TestCase):
    def build_parser(self):
        csslex.getLexer()
        self.parser = cssyacc.parser
    
    def test_cssyacc_benchmark(self):
        self.build_parser()
        f = open("./examples/benchmark.less", 'r')
        result = self.parser.parse(f.read())
        f.close()
        print(result)

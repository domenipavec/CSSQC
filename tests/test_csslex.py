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
import ply.lex as lex
import csslex

data = [
    # sample
    {
        'css': '''body, .bar > .baz {
    color: #333;
    font-size: 14px;
}''',
        'types': [
            'IDENT', 'DELIM', 'WS', 'DELIM', 'IDENT', 'WS', 'DELIM', 'WS', 
            'DELIM', 'IDENT', 'WS', 'BRACES_L', 'WS', 'IDENT', 'COLON', 'WS',
            'HASH', 'SEMICOLON', 'WS', 'IDENT', 'COLON', 'WS', 'DIMENSION',
            'SEMICOLON', 'WS', 'BRACES_R'
        ],
        'values': [
            'body', ',', ' ', '.', 'bar', ' ', '>', ' ', '.', 'baz', ' ', '{',
            '\n    ', 'color', ':', ' ', '#333', ';', '\n    ', 'font-size', ':', ' ',
            '14px', ';', '\n', '}'
        ]
    },
    # comments
    {
        'css': '''/* single line comment */
/* mutli
 * line comment */
// different comment''',
        'types': [
            'COMMENT', 'WS', 'COMMENT', 'WS', 'COMMENT'
        ],
        'values': [
            '/* single line comment */', '\n',
            '/* mutli\n * line comment */', '\n',
            '// different comment'
        ]
    },
    # uri
    {
        'css': 'url("http://test.com/test.css")',
        'types': ['URI'],
        'values': ['url("http://test.com/test.css")']
    },
    # at
    {
        'css': '@media',
        'types': ['ATKEYWORD'],
        'values': ['@media']
    },
    # delims
    {
        'css': ',.&*+>=^$-/!~',
        'types': ['DELIM']*13,
        'values': [',', '.', '&', '*', '+', '>', '=', '^', '$', '-', '/', '!', '~']
    },
    # bad comment
    {
        'css': '/* this comment never ends',
        'types': ['COMMENT'],
        'values': ['/* this comment never ends']
    },
    # bad string
    {
        'css': '"this is a bad string...',
        'types': ['STRING'],
        'values': ['"this is a bad string...']
    },
    # bad url
    {
        'css': 'url("bad url"',
        'types': ['URI'],
        'values': ['url("bad url"']
    }
]

class TestCsslex(unittest.TestCase):
    def build_lexer(self):
        self.lexer = csslex.getLexer()
    
    def perform(self, i):
        self.build_lexer()
        self.lexer.input(data[i]['css'])
        for j,token in enumerate(self.lexer):
            print(token)
            self.assertEqual(data[i]['types'][j], token.type)
            self.assertEqual(data[i]['values'][j], token.value)
    
    def test_csslex_sample(self):
        self.perform(0)
        
    def test_csslex_comments(self):
        self.perform(1)
        
    def test_csslex_url(self):
        self.perform(2)
        
    def test_csslex_at(self):
        self.perform(3)
        
    def test_csslex_delims(self):
        self.perform(4)
    
    def test_csslex_benchmark(self):
        self.build_lexer()
        f = open("./examples/benchmark.less", 'r')
        self.lexer.input(f.read())
        for token in self.lexer:
            print(token)
        f.close()
    
    def test_csslex_badcomment(self):
        self.assertRaises(lex.LexError, self.perform, 5)

    def test_csslex_badstring(self):
        self.assertRaises(lex.LexError, self.perform, 6)

    def test_csslex_badurl(self):
        self.assertRaises(lex.LexError, self.perform, 7)

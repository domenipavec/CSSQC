#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# test_cssyacc.py
# 
# test for parser
# Most examples are from http://lesscss.org/features/
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import unittest
import pprint
import cssyacc
import csslex

from cssyacc.whitespace import Whitespace
from cssyacc.comment import Comment
from cssyacc.statement import Statement
from cssyacc.parentheses import Parentheses
from cssyacc.block import Block
from cssyacc.ruleset import Ruleset
from cssyacc.function import Function
from cssyacc.brackets import Brackets

class TestCssyacc(unittest.TestCase):
    def build_parser(self):
        self.lexer = csslex.getLexer()
        self.parser = cssyacc.parser
    
    def parse(self, s, r):
        print("Test string: ", s)
        
        print("Tokens:")
        l = csslex.getLexer()
        l.input(s)
        for token in l:
            print(token)

        self.build_parser()
        result = self.parser.parse(s, lexer=self.lexer)
        print("Result:\n", result)
        print("Expected result:\n", r)
        self.assertEqual(result,r)
        return result
    
    def test_cssyacc_benchmark(self):
        self.build_parser()
        f = open("./examples/benchmark.less", 'r')
        result = self.parser.parse(f.read(), lexer=self.lexer)
        f.close()
        print(result)

    def test_cssyacc_empty(self):
        self.parse('', [])
    
    def test_cssyacc_ws(self):
        self.parse('\n  \n', [Whitespace('\n  \n')])
    
    def test_cssyacc_comment(self):
        self.parse('''
/* comment */// test 
''', \
            [
                Whitespace('\n'),
                Comment('/* comment */'),
                Comment('// test '),
                Whitespace('\n')
            ])

    def test_cssyacc_statement(self):
        self.parse('''/* statement */
@nice-blue: #5883AD;
''', \
            [
                Comment('/* statement */'),
                Whitespace('\n'),
                Statement(['@nice-blue', ':', Whitespace(' '), '#5883AD']),
                Whitespace('\n')
            ])
    
    def test_cssyacc_multiline_statement(self):
        self.parse('''margin: 0 0
0 0;''', \
            [
                Statement([
                    'margin',
                    ':',
                    Whitespace(' '),
                    '0',
                    Whitespace(' '),
                    '0',
                    Whitespace('\n'),
                    '0',
                    Whitespace(' '),
                    '0'
                ])
            ])
    
    def test_cssyacc_ruleset(self):
        self.parse(''' img[src^="alert"] {
    border: none;
} // comment''', \
            [
                Whitespace(' '),
                Ruleset(['img', Brackets(['src', '^', '=', '"alert"']), Whitespace(' ')], Block([
                    Whitespace('\n    '), 
                    Statement(['border', ':', Whitespace(' '), 'none']),
                    Whitespace('\n')
                ], None)),
                Whitespace(' '),
                Comment('// comment')
            ])

    def test_cssyacc_mixin(self):
        self.parse('''.mixin-class {
  .a( );
}''',   [
            Ruleset(['.', 'mixin-class', Whitespace(' ')], Block([
                Whitespace('\n  '),
                Statement(['.', Function('a(', [Whitespace(' ')])]),
                Whitespace('\n')
            ], None))
        ])
    
    def test_cssyacc_fulltext_statement(self):
        self.parse('''margin@red@{z3}@@dve:#hash.d30 30px 30% url('test')
"str", ( ...;...)[ 3]/* comment */;''', [
            Statement([
                'margin',
                '@red',
                '@{z3}',
                '@@dve',
                ':',
                '#hash',
                '.',
                'd30',
                Whitespace(' '),
                '30px',
                Whitespace(' '),
                '30%',
                Whitespace(' '),
                "url('test')",
                Whitespace('\n'),
                '"str"',
                ',',
                Whitespace(' '),
                Parentheses([Whitespace(' '), '.', '.', '.', ';', '.', '.', '.']),
                Brackets([Whitespace(' '), '3']),
                Comment('/* comment */')
            ])
        ])
    
    def test_cssyacc_block(self):
        r = self.parse('''body{margin:0;padding:0}''', [
            Ruleset(['body'], Block([
                Statement(['margin', ':', '0'])
            ], [
                'padding', 
                ':', 
                '0'
            ]))
        ])
        self.assertNotEqual(r, [
            Ruleset(['body'], Block([
                Statement(['margin', ':', '0'])
            ], None))
        ])

    def test_cssyacc_block_parameter(self):
        self.parse('''header {
  background-color: blue;

  .desktop-and-old-ie( {
    background-color: red;
  });
}''',   [
            Ruleset(['header', Whitespace(' ')], Block([
                Whitespace('\n  '),
                Statement(['background-color', ':', Whitespace(' '), 'blue']),
                Whitespace('\n\n  '),
                Statement(['.', Function('desktop-and-old-ie(', [
                    Whitespace(' '),
                    Block([
                        Whitespace('\n    '),
                        Statement(['background-color', ':', Whitespace(' '), 'red']),
                        Whitespace('\n  ')
                    ], None)
                ])]),
                Whitespace('\n')
            ], None))
        ])
    
    def test_cssyacc_mixin_guard(self):
        self.parse('''.mixin (@a) when (lightness(@a) >= 50%) {
  background-color: black;
}
.mixin (@a) when (lightness(@a) < 50%) {
  background-color: white;
}''',   [
            Ruleset([
                '.',
                'mixin',
                Whitespace(' '),
                Parentheses(['@a']),
                Whitespace(' '),
                'when',
                Whitespace(' '),
                Parentheses([
                    Function('lightness(', ['@a']),
                    Whitespace(' '),
                    '>',
                    '=',
                    Whitespace(' '),
                    '50%'
                ]),
                Whitespace(' ')
            ], Block([
                Whitespace('\n  '),
                Statement([
                    'background-color',
                    ':', 
                    Whitespace(' '),
                    'black'
                ]),
                Whitespace('\n')
            ], None)),
            Whitespace('\n'),
            Ruleset([
                '.',
                'mixin',
                Whitespace(' '),
                Parentheses(['@a']),
                Whitespace(' '),
                'when',
                Whitespace(' '),
                Parentheses([
                    Function('lightness(', ['@a']),
                    Whitespace(' '),
                    '<',
                    Whitespace(' '),
                    '50%'
                ]),
                Whitespace(' ')
            ], Block([
                Whitespace('\n  '),
                Statement([
                    'background-color',
                    ':', 
                    Whitespace(' '),
                    'white'
                ]),
                Whitespace('\n')
            ], None))
        ])

    def test_cssyacc_nesting(self):
        self.parse('''#header {
  color: black;
  .navigation {
    font-size: 12px;
  }
  .logo {
    width: 300px;
  }
}''',   [
            Ruleset(['#header', Whitespace(' ')], Block([
                Whitespace('\n  '),
                Statement(['color', ':', Whitespace(' '), 'black']),
                Whitespace('\n  '),
                Ruleset(['.', 'navigation', Whitespace(' ')], Block([
                    Whitespace('\n    '),
                    Statement(['font-size', ':', Whitespace(' '), '12px']),
                    Whitespace('\n  ')
                ], None)),
                Whitespace('\n  '),
                Ruleset(['.', 'logo', Whitespace(' ')], Block([
                    Whitespace('\n    '),
                    Statement(['width', ':', Whitespace(' '), '300px']),
                    Whitespace('\n  ')
                ], None)),
                Whitespace('\n')
            ], None))
        ])
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

from nose.tools import nottest

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
        self.parser = cssyacc.getYacc()
    
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
    
    @nottest
    def test_cssyacc_benchmark(self):
        self.build_parser()
        f = open("./examples/benchmark.less", 'r')
        result = self.parser.parse(f.read(), lexer=self.lexer)
        f.close()
        print(result)
    test_cssyacc_benchmark.slow = 1

    def test_cssyacc_empty(self):
        self.parse('', [])
    
    def test_cssyacc_ws(self):
        self.parse('\n  \n', [Whitespace('\n  \n', 1)])
    
    def test_cssyacc_comment(self):
        self.parse('''
/* comment */// test 
''', \
            [
                Whitespace('\n', 1),
                Comment('/* comment */', 2),
                Comment('// test ', 2),
                Whitespace('\n', 2)
            ])

    def test_cssyacc_statement(self):
        self.parse('''/* statement */
@nice-blue: #5883AD;
''', \
            [
                Comment('/* statement */', 1),
                Whitespace('\n', 1),
                Statement([('@nice-blue',2), (':',2), Whitespace(' ',2), ('#5883AD',2)], 2),
                Whitespace('\n', 2)
            ])
    
    def test_cssyacc_multiline_statement(self):
        self.parse('''margin: 0 0
0 0;''', \
            [
                Statement([
                    ('margin',1),
                    (':',1),
                    Whitespace(' ',1),
                    ('0',1),
                    Whitespace(' ',1),
                    ('0',1),
                    Whitespace('\n',1),
                    ('0',2),
                    Whitespace(' ',2),
                    ('0',2)
                ], 2)
            ])
    
    def test_cssyacc_ruleset(self):
        self.parse(''' img[src^="alert"] {
    border: none;
} // comment''', \
            [
                Whitespace(' ',1),
                Ruleset([('img',1), Brackets([('src',1), ('^',1), ('=',1), ('"alert"',1)],1,1), Whitespace(' ',1)], Block([
                    Whitespace('\n    ',1), 
                    Statement([('border',2), (':',2), Whitespace(' ',2), ('none',2)], 2),
                    Whitespace('\n', 2)
                ], None, 1, 3)),
                Whitespace(' ', 3),
                Comment('// comment', 3)
            ])

    def test_cssyacc_mixin(self):
        self.parse('''.mixin-class {
  .a( );
}''',   [
            Ruleset([('.',1), ('mixin-class',1), Whitespace(' ',1)], Block([
                Whitespace('\n  ', 1),
                Statement([('.',2), Function('a(', [Whitespace(' ',2)], 2, 2)], 2),
                Whitespace('\n', 2)
            ], None, 1, 3))
        ])
    
    def test_cssyacc_fulltext_statement(self):
        self.parse('''margin@red@{z3}@@dve:#hash.d30 30px 30% url('test')
"str", ( ...;...)[ 3]/* comment */;''', [
            Statement([
                ('margin',1),
                ('@red',1),
                ('@{z3}',1),
                ('@@dve',1),
                (':',1),
                ('#hash',1),
                ('.',1),
                ('d30',1),
                Whitespace(' ',1),
                ('30px',1),
                Whitespace(' ',1),
                ('30%',1),
                Whitespace(' ',1),
                ("url('test')",1),
                Whitespace('\n',1),
                ('"str"',2),
                (',',2),
                Whitespace(' ',2),
                Parentheses([Whitespace(' ',2), ('.',2), ('.',2), ('.',2), (';',2), ('.',2), ('.',2), ('.',2)], 2, 2),
                Brackets([Whitespace(' ',2), ('3',2)], 2, 2),
                Comment('/* comment */', 2)
            ], 2)
        ])
    
    def test_cssyacc_block(self):
        r = self.parse('''body{margin:0;padding:0}''', [
            Ruleset([('body',1)], Block([
                Statement([('margin',1), (':',1), ('0',1)], 1)
            ], [
                ('padding', 1), 
                (':', 1), 
                ('0', 1)
            ], 1, 1))
        ])
        self.assertNotEqual(r, [
            Ruleset([('body',1)], Block([
                Statement([('margin',1), (':',1), ('0',1)], 1)
            ], None, 1, 1))
        ])

    def test_cssyacc_block_parameter(self):
        self.parse('''header {
  background-color: blue;

  .desktop-and-old-ie( {
    background-color: red;
  });
}''',   [
            Ruleset([('header',1), Whitespace(' ', 1)], Block([
                Whitespace('\n  ', 1),
                Statement([('background-color',2), (':',2), Whitespace(' ',2), ('blue',2)], 2),
                Whitespace('\n\n  ', 2),
                Statement([('.',4), Function('desktop-and-old-ie(', [
                    Whitespace(' ', 4),
                    Block([
                        Whitespace('\n    ', 4),
                        Statement([('background-color', 5), (':',5), Whitespace(' ', 5), ('red',5)], 5),
                        Whitespace('\n  ', 5)
                    ], None, 4, 6)
                ], 4, 6)], 6),
                Whitespace('\n', 6)
            ], None, 1, 7))
        ])
    
    def test_cssyacc_mixin_guard(self):
        self.parse('''.mixin (@a) when (lightness(@a) >= 50%) {
  background-color: black;
}
.mixin (@a) when (lightness(@a) < 50%) {
  background-color: white;
}''',   [
            Ruleset([
                ('.',1),
                ('mixin',1),
                Whitespace(' ',1),
                Parentheses([('@a',1)], 1, 1),
                Whitespace(' ', 1),
                ('when',1),
                Whitespace(' ', 1),
                Parentheses([
                    Function('lightness(', [('@a',1)], 1, 1),
                    Whitespace(' ', 1),
                    ('>',1),
                    ('=',1),
                    Whitespace(' ', 1),
                    ('50%',1)
                ], 1, 1),
                Whitespace(' ', 1)
            ], Block([
                Whitespace('\n  ',1),
                Statement([
                    ('background-color',2),
                    (':',2), 
                    Whitespace(' ',2),
                    ('black',2)
                ],2),
                Whitespace('\n',2)
            ], None, 1,3)),
            Whitespace('\n',3),
            Ruleset([
                ('.',4),
                ('mixin',4),
                Whitespace(' ',4),
                Parentheses([('@a',4)], 4, 4),
                Whitespace(' ', 4),
                ('when', 4),
                Whitespace(' ', 4),
                Parentheses([
                    Function('lightness(', [('@a',4)], 4, 4),
                    Whitespace(' ', 4),
                    ('<',4),
                    Whitespace(' ',4),
                    ('50%',4)
                ], 4, 4),
                Whitespace(' ', 4)
            ], Block([
                Whitespace('\n  ', 4),
                Statement([
                    ('background-color',5),
                    (':',5), 
                    Whitespace(' ',5),
                    ('white',5)
                ], 5),
                Whitespace('\n', 5)
            ], None, 4, 6))
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
            Ruleset([('#header',1), Whitespace(' ',1)], Block([
                Whitespace('\n  ', 1),
                Statement([('color',2), (':',2), Whitespace(' ',2), ('black',2)], 2),
                Whitespace('\n  ', 2),
                Ruleset([('.',3), ('navigation',3), Whitespace(' ', 3)], Block([
                    Whitespace('\n    ', 3),
                    Statement([('font-size',4), (':',4), Whitespace(' ', 4), ('12px',4)], 4),
                    Whitespace('\n  ', 4)
                ], None, 3, 5)),
                Whitespace('\n  ', 5),
                Ruleset([('.',6), ('logo',6), Whitespace(' ', 6)], Block([
                    Whitespace('\n    ', 6),
                    Statement([('width',7), (':',7), Whitespace(' ', 7), ('300px',7)], 7),
                    Whitespace('\n  ', 7)
                ], None, 6, 8)),
                Whitespace('\n', 8)
            ], None, 1, 9))
        ])

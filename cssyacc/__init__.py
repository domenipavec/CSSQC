#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssyacc/__init__.py
# 
# yacc parser
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import ply.yacc as yacc

from csslex import tokens

from cssyacc.whitespace import Whitespace
from cssyacc.comment import Comment
from cssyacc.statement import Statement
from cssyacc.parentheses import Parentheses
from cssyacc.block import Block
from cssyacc.ruleset import Ruleset
from cssyacc.function import Function
from cssyacc.brackets import Brackets

# grammer rules
def p_stylesheet(p):
    '''stylesheet : empty
                  | stylesheet CDO
                  | stylesheet CDC
                  | stylesheet ws
                  | stylesheet comment
                  | stylesheet element'''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]

def p_comment(p):
    '''comment : COMMENT'''
    p[0] = Comment(p[1], p.lineno(1))

def p_ws(p):
    '''ws : WS'''
    p[0] = Whitespace(p[1], p.lineno(1))

def p_block(p):
    '''block : BRACES_L elements text BRACES_R'''
    p[0] = Block(p[2], p[3], p.lineno(1), p.lineno(4))

def p_element(p):
    '''element : text block
               | text SEMICOLON'''
    if type(p[2]) is str:
        p[0] = Statement(p[1], p.lineno(2))
    else:
        p[0] = Ruleset(p[1], p[2])

def p_elements(p):
    '''elements : elements element
                | elements ws
                | elements comment
                | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]

def p_text(p):
    '''text : IDENT textsuffix
            | ATKEYWORD textsuffix
            | ATBRACES textsuffix
            | COLON textsuffix
            | HASH textsuffix
            | DELIM textsuffix
            | NUMBER textsuffix
            | DIMENSION textsuffix
            | PERCENTAGE textsuffix
            | URI textsuffix
            | STRING textsuffix
            | UNICODE_RANGE textsuffix
            | INCLUDES textsuffix
            | DASHMATCH textsuffix
            | function textsuffix
            | parentheses textsuffix
            | brackets textsuffix
            | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        if type(p[1]) is str:
            p[0] = [(p[1], p.lineno(1))] + p[2]
        else:
            p[0] = [p[1]] + p[2]

def p_textsuffix(p):
    '''textsuffix : IDENT textsuffix
                  | ATKEYWORD textsuffix
                  | ATBRACES textsuffix
                  | COLON textsuffix
                  | HASH textsuffix
                  | DELIM textsuffix
                  | NUMBER textsuffix
                  | DIMENSION textsuffix
                  | PERCENTAGE textsuffix
                  | URI textsuffix
                  | STRING textsuffix
                  | UNICODE_RANGE textsuffix
                  | INCLUDES textsuffix
                  | DASHMATCH textsuffix
                  | function textsuffix
                  | parentheses textsuffix
                  | brackets textsuffix
                  | ws textsuffix
                  | comment textsuffix
                  | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        if type(p[1]) is str:
            p[0] = [(p[1], p.lineno(1))] + p[2]
        else:
            p[0] = [p[1]] + p[2]

def p_parentheses(p):
    '''parentheses : PARENTHESES_L ptext PARENTHESES_R
                   | PARENTHESES_L ws ptext PARENTHESES_R'''
    if len(p) == 4:
        p[0] = Parentheses(p[2], p.lineno(1), p.lineno(3))
    else:
        p[0] = Parentheses([p[2]] + p[3], p.lineno(1), p.lineno(4))

def p_brackets(p):
    '''brackets : BRACKETS_L text BRACKETS_R
                | BRACKETS_L ws text BRACKETS_R'''
    if len(p) == 4:
        p[0] = Brackets(p[2], p.lineno(1), p.lineno(3))
    else:
        p[0] = Brackets([p[2]] + p[3], p.lineno(1), p.lineno(4))

def p_ptext(p):
    '''ptext : text
             | ptext SEMICOLON textsuffix
             | block'''
    if type(p[1]) is list:
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[1] + [(p[2], p.lineno(2))] + p[3]
    else:
        p[0] = [p[1]]
    

def p_function(p):
    '''function : FUNCTION ptext PARENTHESES_R
                | FUNCTION ws ptext PARENTHESES_R'''
    if len(p) == 4:
        p[0] = Function(p[1], p[2], p.lineno(1), p.lineno(3))
    else:
        p[0] = Function(p[1], [p[2]] + p[3], p.lineno(1), p.lineno(4))

def p_empty(p):
    'empty :'
    pass

# error rule
def p_error(p):
    raise Exception("Syntax error at token " + p.type + " on line " + str(p.lineno))

# build the parser
parser = yacc.yacc(debug=True)

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
                  | stylesheet element'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_block(p):
    '''block : BRACES_L elements text BRACES_R'''
    p[0] = Block(p[2], p[3])

def p_element(p):
    '''element : text block
               | text SEMICOLON'''
    if p[2] == ';':
        p[0] = Statement(p[1])
    else:
        p[0] = Ruleset(p[1], p[2])

def p_elements(p):
    '''elements : elements element
                | elements ws
                | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = p[1] + [p[2]]

def p_text(p):
    '''text : IDENT text
            | ATKEYWORD text
            | ATBRACES text
            | COLON text
            | HASH text
            | DELIM text
            | NUMBER text
            | DIMENSION text
            | PERCENTAGE text
            | URI text
            | STRING text
            | UNICODE_RANGE text
            | INCLUDES text
            | DASHMATCH text
            | function text
            | parentheses text
            | brackets text
            | ws text
            | empty'''
    if len(p) == 2:
        p[0] = []
    else:
        p[0] = [p[1]] + p[2]

def p_parentheses(p):
    '''parentheses : PARENTHESES_L ptext PARENTHESES_R'''
    p[0] = Parentheses(p[2])

def p_brackets(p):
    '''brackets : BRACKETS_L text BRACKETS_R'''
    p[0] = Brackets(p[2])

def p_ptext(p):
    '''ptext : text
             | ptext SEMICOLON text
             | block'''
    if type(p[1]) is list:
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[1] + p[3]
    else:
        p[0] = [p[1]]
    

def p_function(p):
    '''function : FUNCTION ptext PARENTHESES_R'''
    p[0] = Function(p[1], p[2])

def p_ws(p):
    '''ws : COMMENT
          | COMMENT ws
          | WS
          | WS ws'''
    p[0] = Whitespace(p[1])

def p_empty(p):
    'empty :'
    pass

# error rule
def p_error(p):
    raise Exception("Syntax error at token " + p.type + " on line " + str(p.lineno))

# build the parser
parser = yacc.yacc(debug=True)

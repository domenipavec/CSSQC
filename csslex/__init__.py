#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# csslex/__init__.py
# 
# tokenizer for a css file
# Based on: http://www.w3.org/TR/CSS2/syndata.html#tokenization
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

import re
import ply.lex as lex

re.UNICODE = True
re.IGNORECASE = True

tokens = (
    'IDENT',
    'ATKEYWORD',
    'ATBRACES',
    'STRING',
    'HASH',
    'NUMBER',
    'PERCENTAGE',
    'DIMENSION',
    'URI',
    'UNICODE_RANGE',
    'CDO',
    'CDC',
    'COLON',
    'SEMICOLON',
    'BRACES_R',
    'BRACES_L',
    'PARENTHESES_R',
    'PARENTHESES_L',
    'BRACKETS_R',
    'BRACKETS_L',
    'COMMENT',
    'WS',
    'FUNCTION',
    'INCLUDES',
    'DASHMATCH',
    'DELIM'
)

# macros
flags = r'(?iu)'
unicode = r'\\[0-9a-f]{1,6}(\r\n|[ \n\r\t\f])?'
nonascii = r'[^\x00-\xed]'
escape = unicode + r'|\\[^\n\r\f0-9a-f]'
nmchar = r'[_a-z0-9-]|(' + nonascii + r')|(' + escape + r')'
num = r'[0-9]*\.[0-9]+|[0-9]+'
nl = r'\n|\r\n|\r|\f'
w = r'[ \t\r\n\f]*'
string1 = r'"([^\n\r\f\\"]|\\(' + nl + r')|(' + escape + r'))*"'
string2 = r"'([^\n\r\f\\']|\\(" + nl + r')|(' + escape + r"))*'"
string = string1 + r'|' + string2
badstring1 = r'"([^\n\r\f\\"]|\\(' + nl + r')|(' + escape + r'))*\\?'
badstring2 = r"'([^\n\r\f\\']|\\(" + nl + r')|(' + escape + r"))*\\?"
badstring = r'(' + badstring1 + r')|(' + badstring2 + r')'
badcomment1 = r'\/\*[^*]*\*+([^/*][^*]*\*+)*'
badcomment2 = r'\/\*[^*]*(\*+[^/*][^*]*)*'
badcomment = r'(' + badcomment1 + r')|(' + badcomment2 + r')'
baduri1 = r'url\((' + w + r')([!#$%&*-~]|(' + nonascii + r')|(' + escape + r'))*(' + w + ')'
baduri2 = r'url\((' + w + r')(' + string + r')(' + w + r')'
baduri3 = r'url\((' + w + r')(' + badstring + ')'
baduri = r'(' + baduri1 + r')|(' + baduri2 + r')|(' + baduri3 + ')'
nmstart = r'[_a-z]|(' + nonascii + r')|(' + escape + r')'
ident = r'[-]?(' + nmstart + ')(' + nmchar + r')*'
name = r'(' + nmchar + r')+'
comment1 = r'\/\*[^*]*\*+([^/*][^*]*\*+)*\/'
comment2 = r'\/\/[^\n\r\f]*'

# simple rules
t_IDENT = flags + ident
t_ATKEYWORD = flags + r'@+(' + ident + r')'
t_ATBRACES = flags + r'@\{(' + ident + r')\}'
t_HASH = flags + r'\#(' + name + r')'
t_NUMBER = flags + r'(' + num + r')'
t_PERCENTAGE = flags + r'(' + num + r')%'
t_DIMENSION = flags + r'(' + num + r')(' + ident + r')'
t_UNICODE_RANGE = flags + r'u\+[0-9a-f?]{1,6}(-[0-9a-f]{1,6})?'
t_CDO = flags + r'<!--'
t_CDC = flags + r'-->'
t_COLON = flags + r':'
t_SEMICOLON = flags + r';'
t_BRACES_L = flags + r'\{'
t_BRACES_R = flags + r'\}'
t_PARENTHESES_L = flags + r'\('
t_PARENTHESES_R = flags + r'\)'
t_BRACKETS_L = flags + r'\['
t_BRACKETS_R = flags + r'\]'
t_FUNCTION = flags + r'((' + ident + r')|%)\('
t_INCLUDES = flags + r'~='
t_DASHMATCH = flags + r'\|='
t_DELIM = flags + r'[,.&*+><=^$\-/!~]'

# functions

nlregex = re.compile(nl)
def parse_newlines(t):
    t.lexer.lineno += len(nlregex.findall(t.value))

def t_STRING(t):
    parse_newlines(t)
    return t
t_STRING.__doc__ = flags + string

def t_COMMENT(t):
    parse_newlines(t)
    return t
t_COMMENT.__doc__ = flags + r'(' + comment1 + r')|(' + comment2 + r')'

def t_URI(t):
    parse_newlines(t)
    return t
t_URI.__doc__ = flags + r'url\((' + w + ')(' + string + ')(' + w + r')\)'
t_URI.__doc__ += '|url\((' + w + r')([!#$%&*-\[\]-~]|(' + nonascii + r')|(' + escape + r'))*(' + w + r')\)'

def t_WS(t):
    parse_newlines(t)
    return t
t_WS.__doc__ = flags + r'[ \t\r\n\f]+'

# bad and error functions

def t_BAD_STRING(t):
    raise lex.LexError("Bad string in line %i." % t.lexer.lineno, t.lexer.lineno)
t_BAD_STRING.__doc__ = flags + badstring

def t_BAD_URI(t):
    raise lex.LexError("Bad URI in line %i." % t.lexer.lineno, t.lexer.lineno)
t_BAD_URI.__doc__ = flags + baduri

def t_BAD_COMMENT(t):
    raise lex.LexError("Bad comment in line %i." % t.lexer.lineno, t.lexer.lineno)
t_BAD_COMMENT.__doc__ = flags + badcomment

def t_error(t):
    pass
    
# build lexer
lexer = lex.lex()

def getLexer():
    return lexer.clone()

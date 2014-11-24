#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/helpers.py
# 
# Helper functions often used in rules.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssyacc import Block, Brackets, Parentheses, Statement, Function, Ruleset, Whitespace
from cssyacc.selector import Selector

def isTupleWithValues(token, values):
    if type(token) is tuple:
        for value in values:
            if token[0] == value:
                return True
    return False

def isTupleWithValue(token, value):
    return type(token) is tuple and token[0] == value

def isLast(i, tokens):
    return i == len(tokens) - 1

def inspectWhitespaces(data, cb):
    if type(data) is Block:
        for el in data.elements:
            i = inspectWhitespaces(el, cb)
            if i != -1:
                return i
    elif type(data) is Brackets \
        or type(data) is Parentheses \
        or type(data) is Selector \
        or type(data) is Statement:
        for t in data.text:
            i = inspectWhitespaces(t, cb)
            if i != -1:
                return i
    elif type(data) is Function:
        for n in data.name:
            i = inspectWhitespaces(n, cb)
            if i != -1:
                return i
        for t in data.text:
            i = inspectWhitespaces(t, cb)
            if i != -1:
                return i
    elif type(data) is Whitespace:
        if not cb(data):
            return data.lineno
    return -1

def isSpacesOnly(v):
    for x in v:
        if x != ' ':
            return False
    return True

def isProperty(s):
    i = 0
    # property name
    if not (type(s.text[i]) is tuple \
            and len(s.text[i][0]) > 1) \
        or isLast(i, s.text):
        return False
    i += 1
    # optional ws
    if type(s.text[i]) is Whitespace:
        if isLast(i, s.text):
            return False
        i += 1
    # colon
    if not isTupleWithValue(s.text[i], ':') \
        or isLast(i, s.text):
        return False
    i += 1
    # optional ws
    if type(s.text[i]) is Whitespace:
        if isLast(i, s.text):
            return False
        i += 1
    # value
    if not type(s.text[i]) is tuple:
        return False
    else:
        return True
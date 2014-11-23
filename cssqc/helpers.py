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
            if not inspectWhitespaces(el, cb):
                return False
        if not inspectWhitespaces(data.last, cb):
            return False
    elif type(data) is Brackets \
        or type(data) is Parentheses \
        or type(data) is Selector \
        or type(data) is Statement:
        for t in data.text:
            if not inspectWhitespaces(t, cb):
                return False
    elif type(data) is Function:
        for n in data.name:
            if not inspectWhitespaces(n, cb):
                return False
        for t in data.text:
            if not inspectWhitespaces(t, cb):
                return False
    elif type(data) is Ruleset:
        for s in data.selectors:
            if not inspectWhitespaces(s, cb):
                return False
        if not inspectWhitespaces(data.block, cb):
            return False
    elif type(data) is Whitespace:
        if not cb(data):
            return False
    return True
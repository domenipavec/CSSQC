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
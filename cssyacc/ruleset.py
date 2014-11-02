#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssyacc/ruleset.py
# 
# class for ruleset
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

class Ruleset:
    def __init__(self, n, b):
        if n is None:
            self.name = []
        else:
            self.name = n
        self.block = b
    
    def __str__(self):
        return ''.join(map(str, self.name)) + ': ' + str(self.block)
    
    def __len__(self):
        return len(self.block)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.name == other.name and self.block == other.block

    def __repr__(self):
        return '<Ruleset>\n    <Name>\n        ' + '\n        '.join(map(repr, self.name)) \
            + '\n    </Name>\n' + repr(self.block) + '\n</Ruleset>'
        
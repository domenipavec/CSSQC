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

import cssqc.parser
from cssyacc.selector import Selector

class Ruleset:
    def __init__(self, name, b):
        self.selectors = []
        if name is not None:
            prev = 0
            for i in range(len(name)):
                if type(name[i]) is tuple \
                    and name[i][0] == ',':
                    self.selectors.append(Selector(name[prev:i], name[i][1]))
                    prev = i + 1
            self.selectors.append(Selector(name[prev:len(name)], b.lb_lineno))
        self.block = b

        i = cssqc.parser.CSSQC.getInstance()
        if i is not None:
            i.event(self.__class__.__name__, self)
    
    def __str__(self):
        return ''.join(map(str, self.selectors)) + ': ' + str(self.block)
    
    def __len__(self):
        return len(self.block)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.selectors == other.selectors and self.block == other.block

    def __repr__(self):
        return '<Ruleset>\n    <Name>\n        ' + '\n        '.join(map(repr, self.selectors)) \
            + '\n    </Name>\n' + repr(self.block) + '\n</Ruleset>'
        

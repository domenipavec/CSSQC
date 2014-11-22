#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noOverqualifying.py
# 
# Do not overqualifying.
# Options are 'class', 'id', 'both'.
# Class means no tag with class, but only if there are not 2
# different rules for different tags with same class.
# (e.g. div.class, but allowed div.class {} span.class {})
# ID means nothing additional when using ID qualifier (e.g. div#id.class)
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from csslex import t_IDENT
from cssyacc import Whitespace, Comment

import re

def getHelp():
    return """Do not allow overqualifying. Options are 'class', 'id' and 'both'.
Class means no tag with class, but only if there are not 2 different rules for different tags with same class.
ID means nothing additional when using ID qualifier."""

class noOverqualifying:
    def __init__(self, data):
        self.check_class = False
        self.check_ID = False
        if data == 'class':
            self.check_class = True
        elif data == 'id':
            self.check_ID = True
        elif data == 'both':
            self.check_class = True
            self.check_ID = True
        else:
            raise Exception('Invalid input for rule noOverqualifying.')
        self.ident_re = re.compile(t_IDENT)
        # format for class_list is [number_of_tags, line_number, tag]
        self.class_list = {}

    def afterParse(self, result):
        warnings = []
        for class_name in self.class_list:
            if self.class_list[class_name][0] == 1:
                warnings.append(QualityWarning('noOverqualifying', \
                   self.class_list[class_name][1],
                   'Overqualified class "%s.%s".' % (self.class_list[class_name][2], class_name)))
        return warnings

    def on_Selector(self, s):
        for i in range(len(s.text)):
            if type(s.text[i]) is tuple:
                if self.check_class:
                    if self.isTagClassPair(s, i):
                        return []
                if self.check_ID:
                    if self.isOverqualifiedID(s, i):
                        return [QualityWarning('noOverqualifying', \
                                               s.text[i][1], \
                                               'Overqualified ID "%s".' % s.text[i][0])]
        return []
    
    def isOverqualifiedID(self, s, i):
        if s.text[i][0][0] == '#':
            for j in range(len(s.text)):
                if i != j and \
                    (type(s.text[j]) is not Comment and type(s.text[j]) is not Whitespace):
                    return True
        return False
    
    def isTagClassPair(self, s, i):
        try:
            class_name = s.text[i+1][0]
            tag_name = s.text[i-1][0]
            if s.text[i][0] == '.' \
                and self.ident_re.match(class_name) \
                and self.ident_re.match(tag_name):
                if class_name in self.class_list:
                    if self.class_list[class_name][2] != tag_name:
                        self.class_list[class_name][0] += 1
                else:
                    self.class_list[class_name] = [1, s.text[i][1], tag_name]
                return True
        except Exception as inst:
            pass
        return False

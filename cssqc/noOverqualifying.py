#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/noOverqualifying.py
# 
# Do not overqualifying.
# Options are ['class'], ['id'], ['class', 'id'], ['both'].
# Last two are identical.
# Class means no tag with class, but only if there are not 2
# different rules for different tags with same class.
# (e.g. div.class, but allowed div.class {} span.class {})
# ID means nothing additional when using ID qualifier (e.g. div#id.class)
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc import QualityWarning
from csslex import t_IDENT
from cssyacc import Whitespace, Comment

import re

class noOverqualifying:
    def __init__(self, data):
        self.check_class = False
        self.check_ID = False
        if 'class' in data:
            self.check_class = True
        if 'id' in data:
            self.check_ID = True
        if 'both' in data:
            self.check_class = True
            self.check_ID = True
        self.ident_re = re.compile(t_IDENT)
        # format for class_list is [number_of_tags, line_number, tag]
        self.class_list = {}

    def afterParse(self):
        warnings = []
        print(self.class_list)
        for class_name in self.class_list:
            if self.class_list[class_name][0] == 1:
                warnings.append(QualityWarning('noOverqualifying', \
                   self.class_list[class_name][1],
                   'Overqualified class "%s.%s".' % (self.class_list[class_name][2], class_name)))
        return warnings

    def on_Ruleset(self, rs):
        for i in range(len(rs.name)):
            if type(rs.name[i]) is tuple:
                if self.check_class:
                    if self.isTagClassPair(rs, i):
                        return []
                if self.check_ID:
                    if self.isOverqualifiedID(rs, i):
                        return [QualityWarning('noOverqualifying', \
                                               rs.name[i][1], \
                                               'Overqualified ID "%s".' % rs.name[i][0])]
        return []
    
    def isOverqualifiedID(self, rs, i):
        if rs.name[i][0][0] == '#':
            for j in range(len(rs.name)):
                if i != j and \
                    (type(rs.name[j]) is not Comment and type(rs.name[j]) is not Whitespace):
                    return True
        return False
    
    def isTagClassPair(self, rs, i):
        try:
            class_name = rs.name[i+1][0]
            tag_name = rs.name[i-1][0]
            if rs.name[i][0] == '.' \
                and self.ident_re.match(class_name) \
                and self.ident_re.match(tag_name):
                if class_name in self.class_list:
                    if self.class_list[class_name][2] != tag_name:
                        self.class_list[class_name][0] += 1
                else:
                    self.class_list[class_name] = [1, rs.name[i][1], tag_name]
                return True
        except:
            pass
        return False

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
        self.oq_class = False
        self.oq_id = False
        if 'class' in data:
            self.oq_class = True
        if 'id' in data:
            self.oq_id = True
        if 'both' in data:
            self.oq_class = True
            self.oq_id = True
        self.ident_re = re.compile(t_IDENT)
        self.tag_class_pairs = {}

    def afterParse(self):
        warnings = []
        for c in self.tag_class_pairs:
            if self.tag_class_pairs[c][0] == 1:
                warnings.append(QualityWarning('noOverqualifying', \
                                               self.tag_class_pairs[c][1],
                                               'Overqualified class "%s.%s".' % (self.tag_class_pairs[c][2], c)))
        return warnings

    def on_Ruleset(self, rs):
        for i in range(len(rs.name)):
            if type(rs.name[i]) is tuple:
                if self.oq_class:
                    if self.checkClass(rs, i):
                        return []
                if self.oq_id:
                    if self.checkID(rs, i):
                        return [QualityWarning('noOverqualifying', \
                                               rs.name[i][1], \
                                               'Overqualified ID "%s".' % rs.name[i][0])]
        return []
    
    def checkID(self, rs, i):
        if rs.name[i][0][0] == '#':
            for j in range(len(rs.name)):
                if i != j and \
                    (type(rs.name[j]) is not Comment and type(rs.name[j]) is not Whitespace):
                    return True
        return False
    
    def checkClass(self, rs, i):
        try:
            if rs.name[i][0] == '.' \
                and self.ident_re.match(rs.name[i+1][0]) \
                and self.ident_re.match(rs.name[i-1][0]):
                ident = rs.name[i+1][0]
                if ident in self.tag_class_pairs:
                    if self.tag_class_pairs[ident][2] != rs.name[i-1][0]:
                        self.tag_class_pairs[ident][0] += 1
                else:
                    self.tag_class_pairs[ident] = [1, rs.name[i][1], rs.name[i-1][0]]
                return True
        except:
            pass
        return False
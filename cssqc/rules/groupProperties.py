#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/groupProperties.py
# 
# Group properties.
# Groups are defined in cssqc/group/*.dat.
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssyacc import Whitespace, Statement
from cssqc.helpers import isProperty

from pkg_resources import resource_string

def getHelp():
    return """Group properties.
Grouping rules are defined in cssqc/group/*.dat. OPT must be valid grouping name."""

class groupProperties:
    def __init__(self, data):
        self.groups = []
        o = resource_string('cssqc', 'group/' + data + '.dat').decode('utf-8')
        for line in o.split('\n'):
            self.groups.append(set(line.split(' ')))

    def on_Ruleset(self, rs):
        warnings = []
        group_id = -1
        newlines = 0
        for el in rs.block.elements:
            if type(el) is Statement \
                and isProperty(el):
                # reset newlines count
                newlines = 0
                
                pname = el.text[0][0]
                
                # get property group
                pgroup = -1
                for i in range(len(self.groups)):
                    if pname in self.groups[i]:
                        pgroup = i
                        break
                
                # unknown group skip
                if pgroup == -1:
                    continue
                
                # new group started
                if group_id == -1:
                    group_id = pgroup
                    continue
                # check if belongs in existing group
                else:
                    if pgroup != group_id:
                        warnings.append(QualityWarning('groupProperties', el.text[0][1], \
                            'Property in wrong group.'))
            elif type(el) is Whitespace:
                # start new group after 2 newline without statements
                newlines += el.value.count('\n')
                if newlines > 1:
                    group_id = -1

        return warnings
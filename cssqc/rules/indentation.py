#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# cssqc/indentation.py
# 
# Do not allow descendant selectors.
# (e.g. div > a {} is ok, but div a {} is not)
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from cssqc.qualityWarning import QualityWarning
from cssqc.helpers import inspectWhitespaces, isLast
from cssyacc import Whitespace, Statement

def getHelp():
    return """Ensure proper indentation. OPT can be integer number of spaces or 'tab'.
Allows right align for properties with same suffix."""

class indentation:
    def __init__(self, data):
        if data == 'tab':
            self.indent = '\t'
        else:
            self.indent = ' '*int(data)

    def afterParse(self, result):
        warnings = []
        
        # parse everything not in rulesets
        for el in result:
            ln = inspectWhitespaces(el, \
                    lambda ws: (not '\n' in ws.value) or ws.value.endswith('\n'))
            if ln != -1:
                warnings.append(QualityWarning('indentation', ln+1, \
                    'Incorrect indentation outside of block.'))

        return warnings

    def on_Ruleset(self, rs):
        warnings = []
        
        # parse selector indent
        for s in rs.selectors:
            ln = inspectWhitespaces(s, lambda ws: (not '\n' in ws.value) or ws.value.endswith('\n'+self.indent*rs.depth))
            if ln != -1:
                warnings.append(QualityWarning('indentation', ln+1, \
                    'Incorrect indentation in selector.'))
        
        # vars for align enable
        carry = 0
        last_length = 0
        last_suffix = ''
        
        # parse block elements
        for i in range(len(rs.block.elements)):
            el = rs.block.elements[i]

            # last whitespace is for closing brace
            if isLast(i, rs.block.elements) \
                and type(el) is Whitespace \
                and len(rs.block.last.text) == 0:
                if not (('\n' not in el.value) or el.value.endswith('\n'+self.indent*rs.depth)):
                    warnings.append(QualityWarning('indentation', el.lineno+1, \
                        'Incorect indentation of closing braces.'))
                    
            # whitespace can have additional spaces for alignment
            elif type(el) is Whitespace:
                if not (('\n' not in el.value) or el.value.endswith('\n'+self.indent*(rs.depth+1))):
                    nextElement = None
                    if isLast(i, rs.block.elements):
                        nextElement = rs.block.last
                    else:
                        nextElement = rs.block.elements[i+1]
                    
                    if type(nextElement) is Statement \
                        and type(nextElement.text[0]) is tuple \
                        and nextElement.text[0][0].endswith(last_suffix) \
                        and el.value.endswith('\n'+self.indent*(rs.depth+1)+' '*(last_length - len(nextElement.text[0][0]))):
                        carry = (last_length - len(nextElement.text[0][0]))
                    else:
                        warnings.append(QualityWarning('indentation', el.lineno+1, \
                            'Incorect indentation in block.'))
            
            # store first tuple length and suffix for alignment
            elif type(el) is Statement:
                if type(el.text[0]) is tuple:
                    last_length = carry + len(el.text[0][0])
                    last_suffix = el.text[0][0][-5:]
                    carry = 0

                ln = inspectWhitespaces(el, \
                    lambda ws: (not '\n' in ws.value) or ws.value.endswith('\n'+self.indent*(rs.depth+1)))
                if ln != -1:
                    warnings.append(QualityWarning('indentation', ln+1, \
                        'Incorect indentation in block.'))
            
            # parse everything else
            else:
                ln = inspectWhitespaces(el, \
                    lambda ws: (not '\n' in ws.value) or ws.value.endswith('\n'+self.indent*(rs.depth+1)))
                if ln != -1:
                    warnings.append(QualityWarning('indentation', ln+1, \
                        'Incorect indentation in block.'))
        
        # parse last statement of block
        for i in range(len(rs.block.last.text)):
            el = rs.block.last.text[i]
            
            if isLast(i, rs.block.last.text) \
                and type(el) is Whitespace:
                if not (('\n' not in el.value) or el.value.endswith('\n'+self.indent*rs.depth)):
                    warnings.append(QualityWarning('indentation', el.lineno+1, \
                        'Incorect indentation in last statement.'))
            else:
                ln = inspectWhitespaces(el, \
                    lambda ws: (not '\n' in ws.value) or ws.value.endswith('\n'+self.indent*(rs.depth+1)))
                if ln != -1:
                    warnings.append(QualityWarning('indentation', ln+1, \
                        'Incorect indentation of closing braces.'))
            
        return warnings

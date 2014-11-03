#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------
# setup.py
# 
# setup for CSSQC
# ----------------------------------------------------------------
# copyright (c) 2014 - Domen Ipavec
# Distributed under The MIT License, see LICENSE
# ----------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name='CSSQC',
    
    version='0.1',
    
    packages=['csslex', 'cssyacc'],
    
    test_suite='nose.collector',
    
    install_requires=['nose', 'ply']
)

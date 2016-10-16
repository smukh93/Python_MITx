# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:09:49 2016

@author: pia-hp
"""

#define the simple_divide function here
def simple_dividde(item, denom):
    try:
        return item/denom
    except ZeroDivisionError:
        return 0

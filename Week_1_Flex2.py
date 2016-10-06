# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 00:33:31 2016

@author: pia-hp
"""

c = "str"
varA = -8
varB = "goodbye"
if (type(varA) == type(c))| (type(varB) == type(c)):
        print('string involved')
else:
    if varA > varB:
        print("bigger")
    elif varA == varB:
        print("equal")
    else:
        print("smaller")
        
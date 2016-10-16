# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:05:27 2016

@author: pia-hp
"""
def deep_reverse(listA):
    for inside_list in listA:
        inside_list.reverse()
    listA.reverse()
    return listA
    
print(deep_reverse([[1,2], [3], [4,5,6]]))
print(deep_reverse( [[1, 2], [3, 4], [5, 6, 7]]))
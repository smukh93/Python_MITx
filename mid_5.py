# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:05:27 2016

@author: pia-hp
"""
def dot_product(listA, listB):
    total = 0
    for i in range(len(listA)):
        total+= listA[i]*listB[i]
    return total
    
    
print("The dot product is ",dot_product([1, 2, 3],[4,5,6]))
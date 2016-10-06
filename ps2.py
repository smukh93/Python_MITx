# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:39:30 2016

@author: pia-hp
"""

s=input('Enter string: ')
x ='bob'
count = 0
flag = True
start = 0
while flag:
    a = s.find(x,start)
    if a == -1:
        flag = False
    else:
        count+=1
        start=a+1
print(count)
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:39:30 2016

@author: pia-hp
"""

""" Write a program that prints the longest substring of s in which the
 letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
 then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc"""

s = input('Enter string: ')
length = 1
max_len = 1
start = 0
for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        length+=1
    else:
        length = 1
    if length > max_len:
        max_len = length
        start = i + 2 - max_len
print ("Longest substring of the string in alphabetical order: " + s[start:start+max_len])

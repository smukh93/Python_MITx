# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:30:39 2016

@author: pia-hp
"""

s = input('Enter string:')
num_vowels = 0
for x in s:
    if (x=='a') | (x=='e') | (x=='o') | (x == 'i') | (x =='u'):
      num_vowels+=1
print(num_vowels)

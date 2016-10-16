# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 14:37:08 2016

@author: pia-hp
"""

def genPrimes():
    primes = []
    last = 1
    while(True):
        last+=1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
            
print(genPrimes())
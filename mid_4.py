# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 22:05:27 2016

@author: pia-hp
"""
import math
def closest_power(base,num):
    if num == 1:
        return 0
    else:
        exp = 1
        while True:
            if num == int(math.pow(base,exp)):
                return exp
                break
            elif num > int(math.pow(base,exp)):
                lower = int(math.pow(base,exp))
                upper = int(math.pow(base,exp+1))
                ans = exp
            else:
                break
            exp+=1
        diff_upper = num - lower
        diff_lower = upper - num
        if diff_upper < diff_lower:
             return (ans)
        else:
             return (ans+1)
        
print(closest_power(3,12))
print(closest_power(4,12))
print(closest_power(4,1))
print(closest_power(5,25))
print(closest_power(16,22))
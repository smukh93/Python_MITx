# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 11:19:59 2016

@author: pia-hp
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self,other):
        """ Returns common elements between two sets"""
        new_set = intSet()
        for val in self.vals:
           if other.member(val):
               new_set.insert(val)
        return new_set
       
    def __len__(self):
        """ Returns length of the set """
        return len(self.vals)
        
        
#Test cases
        
set1 = intSet()
print(set1)
set1.insert(4)
set1.insert(5)
print(set1)
set2 = intSet()
print(set1.intersect(set2))
set2.insert(4)
print(set1.intersect(set2))
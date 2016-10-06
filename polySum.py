"""A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 0.25∗n∗s2tan(π/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. 
This function should sum the area and square of the perimeter of the 
regular polygon. The function returns the sum, rounded to 4 decimal places.
""" 

#importing math for calculations

import math

#Calculating Square of a given number

def square(x):
    return x**2

#Area of a regular polygon
    
def area(n,s):
    return (0.25 * n * square(s) ) / (math.tan(math.pi/n))
    
#calculating perimeter of  a regular polygon
    
def perimeter(n,s):
    return n*s

#calculating the required function Polysum: sum the area and square of the perimeter of the 
#regular polygon.

def polysum(n,s):
    return round(area(n,s)+square(perimeter(n,s)),4)
    
    
""" Testing    
print(square(2))
print(area(3,2))
print(perimeter(3,2))
print(polysum(3,2))
"""
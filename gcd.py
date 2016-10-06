def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    while b:
        a,b = b, a %b
    return abs(a)
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    return gcdRecur(b , a%b) if b else abs(a)

print("GCD Iterative: " +str(gcdIter(12,6)))
print("GCD Recursive: "+ str(gcdRecur(12,6)))

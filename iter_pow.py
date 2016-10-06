def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    prod = 1
    if exp == 0:
        return 1
    else:
        for x in range(exp):
            prod *=base
        return prod


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
         return base * recurPower(base,exp-1)
   

exp = int(input('Enter exp: '))
base = int(input('Enter base: '))
print(iterPower(base,exp))
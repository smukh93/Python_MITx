def f(i):
    return i + 2
def g(i):
    return i > 5

#g(f(i)) should return true for each i in L
def applyF_filterG(L,f,g):
    new_list = []
    for i in L:
        if g(f(i))==True:
            new_list.append(i)
    L[:] = new_list
    return max(new_list) 
L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)
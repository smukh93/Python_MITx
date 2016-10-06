def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
  
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2  
   
def a1(x, y, z):
     if x:
         return y
     else:
         return z

def b1(q, r):
    return a(q>r, q, r)
    
print(a1(3>2, a1, b1))

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
print(foo(3,0))

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

print(foo(2))
'''
Created on Feb 18, 2014

@author: khiemtd
'''

class Vector: 
    def __init__(self, a, b):
        self.a = a 
        self.b = b 
    def __str__(self): 
        return 'Vector (%d, %d)' % (self.a, self.b) 
    def __add__(self,other): 
        return Vector(self.a + other.a, self.b + other.b) 
 
v1 = Vector(2,10) 
print v1
v2 = Vector(5,-2)
print v2 
print v1 + v2 
''' overload mean modify function build in --'''
for i in range(1,4):
    print i
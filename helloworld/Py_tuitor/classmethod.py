'''
Created on Oct 17, 2014

@author: khiemtd
'''
class A(object): #cls first argument for instance
    def printf(self,str):
        print (str)

class B(A):# cls first argument for class 
    @classmethod
    def run(self):#maybe cls
        a= A()
        a.printf('abc')
        

B.run()
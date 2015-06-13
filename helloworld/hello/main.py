'''
Created on Feb 14, 2014

@author: khiemtd
'''
#import module
#from package import module
from classa1 import a1
#import classa1 
#reload(classa1)
'''Python imports (loads) a module only once per process, by default, so if you have
changed its source code and want to run the new version without stopping and
restarting Python, you will have to reload it. You must import a module at least once
before you can reload it. Running files of code from a system shell command line,
via an icon click, or via an IDE such as IDLE generally makes this a nonissue, as
those launch schemes usually run the current version of the source code file each
time.

mutual: tuple, number, string
immutual: the others

conver number to ASCII, ,,: ord, chr'''
import sys, time # include stdout, stdin...

start=time.clock()
print sys.platform+'\nPythoon version '+ sys.version
print "hello world"
print 3+5, 0xf5
name='violet'
name=name.upper()
print name + " la ai" +"?"+'ff'.upper()
x=34.556565656565
#nam=int(raw_input())
print name +str(x)             #not print name+34
print name ,"%.1f" % (x)+"' tron'"
print 'Ni'*10
# xem thuoc trong 4 datatype x=2>> type(x), x=2./3
s='e23'
print s[-2:] 
print s[:2]

l=[1,2,3]      
k=range(4,17,3)
for i in l:    #Loop
    print i
for i in k:
    print i

x=3
while x>0:
    print x
    x=x-1

try:
    print 1/0
except ZeroDivisionError:  #ten default san co
    print "loi"
try:
    open('fdf')
except IOError, (ErrorNumber, ErrorMessage):
    if ErrorNumber==2:
        print "file not found"
    else:
        print "congratulation"
#x=input('sdsds') khac raw_input('dfdfdfd')
#lambda argument1, argument2,... argumentN : expression using arguments
f=lambda x:x**x
print 'dung lambda'+str(f(3))
y=None
while not y:
    try:
        y=int(raw_input('nhap y'))
    except ValueError:
        print "invalid num"

f=open('text.txt','w')
f.write('hello')
f.write('\ndfdfd')
#ff=open('text.txt','r').read()
#for line in f:
#    print line              #==print ff

f.close()


write=sys.stdout.write
write('20')
write('05\n')

import math
print math.sqrt(40)
print math.sin(20)

class Foo:
    def setx(self,x):
        self.x=x
    def bar(self):
        print self.x
f=Foo()
f.setx(5)
f.bar()
vars(Foo)

class a2(a1):
    def pri2(self):
        print "classa2"
        a1.pri1(self)
    x2=3
g=a2()
a2.pri2(g)
print g.x1
print g.x2
class A1:
    def __init__(self,so):
        print str(so)+"co init"
a10=A1(99)               #truyen thang ko goi ham
class Ako__int:
    def setx(self,so):
        print str(so)+ "ko cos init"
a20=Ako__int()
a20.setx(100)

import random
#from time import clock
print random.randint(1,100)

l1=[1,2,3]
l2=[4,5,6]
print 'in l1 *l2'+ str([x*y for x in l1 for y in l2])
print [x for x in l1 if 1<x<4]
any([i%3 for i in l1])

stop=time.clock()
print stop-start



        
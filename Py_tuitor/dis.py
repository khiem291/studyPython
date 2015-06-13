'''
Created on Oct 23, 2014

@author: khiemtd
'''
#!/usr/bin/python 
import dis
 
def sum(): 
   vara = 10 
   varb = 20 
 
   sum = vara + varb 
   print "vara + varb = %d" % sum 
 
# Call dis function for the function. 
 
dis.dis(sum) 

import pdb
import temp
pdb.run('temp')

#or python -m pdb myscript.py
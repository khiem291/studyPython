#!/usr/bin/python
'''
Created on Dec 2, 2014

@author: khiemtd
'''

#from sys import argv
#print 'input ', argv[1:]

'This program print line contain word usb'
#===============================================================================
# f=open('/var/log/dmesg')
# 
# for line in f.readlines():
#     if line.find('usb') != -1:
#         print line
# 
# f.close() 
#===============================================================================

# other method
import re
temp= re.compile('usb')
f=open('/var/log/dmesg')

for line in f.readlines():
    if temp.search(line):

        print line
f.close()
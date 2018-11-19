'''
Created on Oct 26, 2014

@author: khiemtd
'''
from socket import *
import sys


servhost = 'localhost'
port = 1234

message = ['testting debug']
if len(sys.argv[1])>1:
    servhost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])
        
obj = socket(AF_INET, SOCK_STREAM)
obj.connect((servhost, port))
for line in message:
    obj.send(line)
    data = obj.recv(1024)
    print 'data recv: ', data
file = obj.makefile('r')
sys.stdout = file

obj.close()
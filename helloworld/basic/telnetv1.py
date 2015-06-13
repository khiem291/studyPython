#!/usr/local/bin/python 
'''
Created on Feb 15, 2014

@author: khiemtd
'''
import telnetlib

host='172.33.44.155'
user='root'
passwr=None

tn=telnetlib.Telnet(host)
tn.read_until("login:",5)   #read until string time out
tn.write(user+ "\n")
'''
if passwr=="":
    tn.read_until("Password:")
    tn.write(passwr+"\n")
else:
    print "incorrect pass"
'''
tn.write('cd /home \n')
#tn.write("/home/ATVN_Eng/af5xxx/16_af5pon0011_ce02/ep5ace24/sdk/epapp\n")
tn.write("ls\n")
tn.write("exit\n")
print tn.read_all()
tn.close()
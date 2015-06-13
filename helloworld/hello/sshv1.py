'''
Created on Feb 15, 2014

@author: khiemtd
'''


import pxssh

host='172.33.34.42'
user='khiemtd'
passwr='kodatpass'

ss=pxssh.pxssh()
if not ss.login(host,user,passwr):
    print "ssh fail"
else:
    print "ssh successful"
    #ss.split_command_line('ls\n')
    ss.sendline('ls;df')
    ss.prompt()
    print ss.before

ss.logout()



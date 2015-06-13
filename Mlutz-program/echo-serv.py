'''
Created on Oct 26, 2014

@author: khiemtd
'''
from socket import *
import thread
import time
host = '' #mean all
port = 1234

obj = socket(AF_INET,SOCK_STREAM)
obj.bind((host,port))#tuble
obj.listen(5)
print 'Server %s listening port: %s'%(gethostbyname(gethostname()),port)

def now():
    return time.ctime(time.time())

def handle(conn):
    time.sleep(5)
    while True:
        data = conn.recv(1024)
        #time.sleep(3) rise to 8 client: 2 will be fail connect
        if not data: break
        conn.send('Echo=>' + data)
    conn.close()

def dispatcher():
    while True:
        conn, address = obj.accept()
        print('Server connected by', address, ' ')
        print('at', now())
        thread.start_new_thread(handle, (conn,))
dispatcher()
    

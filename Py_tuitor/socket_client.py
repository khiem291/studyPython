'''
Created on Oct 14, 2014

@author: khiemtd
'''
#!/usr/bin/python           # This is client.py file 
 
import socket               # Import socket module 
 
s = socket.socket()         # Create a socket object 
host = socket.gethostname() # Get local machine name
print 'Localhost:',host
# host Linux 44
host = '172.33.34.42' 
port = 12345                # Reserve a port for your service. 
 
s.connect((host, port)) 
print s.recv(1024) 
s.close()                     # Close the socket when done 


'''
Server
#!/usr/bin/python           # This is server.py file 
 
import socket               # Import socket module 
 
s = socket.socket()         # Create a socket object 
host = socket.gethostname() # Get local machine name 
port = 12345                # Reserve a port for your service. 
s.bind((host, port))        # Bind to the port 
 
s.listen(5)                 # Now wait for client connection. 
while True: 
   c, addr = s.accept()     # Establish connection with client. 
   print 'Got connection from', addr #address +port (xx,xx)
   c.send('Thank you for connecting') 
   c.close()                # Close the connection 
'''
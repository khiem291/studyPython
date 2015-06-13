'''
Created on Feb 14, 2014

@author: khiemtd
'''

import socket
import sys
import telnetlib
from telnetlib import Telnet

#s=socket.socket()
#s.connect('172.33.33.151',23) #client


class taoketnoi:
    
    def __init__(self,ipadd,port,mode):
        pass
    def opensocket(self):
        skt=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        try:
            skt.connect(self.ipadd, self.port)
        except socket.error,e:
            print "Fail to connect %s %d %d " % (self.ipadd,self.port,self.mode)
            sys.exit()
        try:
            skt.setblocking(self.mode)
        except socket.error,e:
            print "fail to set blocking", e
            sys.exit()

tt=taoketnoi(ipadd='172.33.44.155', port=23,mode=1)


'''##util
import telnetlib
class ATTelnetController:
    def __init__(self, host_name, user_name, password, port=23, logfile=None):
        self.host_name          = host_name
        self.user_name          = user_name
        self.password           = password
        self.port               = port
        self.logfile            = logfile

        self.telnetSession      = None
        self.defaultPrompt      = r"[#$>]"
        self.defaultTimeout     = 5
        self.unexpectedValue    = ''


    def connect(self):
        try:
            self.telnetSession = telnetlib.Telnet(self.host_name, port=self.port)
            result = self.telnetSession.expect([self.defaultPrompt,], timeout=self.defaultTimeout)
            if int(result[0] < 0):
                return None
            else:
                return self.telnetSession
        except Exception as e:
            print e
            return None



    def run_command(self, command, timeout=10, prompt=']$'):
        """ Run a command on the remote host.

            @param command: Unix command
            @return: Command output
            @rtype: String
        """
        self.telnetSession.write(command + '\n')
        response = self.telnetSession.read_until(prompt, timeout=timeout)
        return self.__strip_output(command, response)


    def disconnect(self):
        """ Close the connection to the remote host. """
        self.telnetSession.close()


    def run_atomic_command(self, command):
        """ Connect to a remote host, login, run a command, and close the connection.

            @param command: Unix command
            @return: Command output
            @rtype: String
        """
        self.login()
        command_output = self.run_command(command)
        self.logout()
        return command_output


    def __strip_output(self, command, response):
        """ Strip everything from the response except the actual command output.

            @param command: Unix command
            @param response: Command output
            @return: Stripped output
            @rtype: String
        """
        lines = response.splitlines()
        # if our command was echoed back, remove it from the output
        if command in lines[0]:
            lines.pop(0)
        # remove the last element, which is the prompt being displayed again
        lines.pop()
        # append a newline to each line of output
        lines = [item + '\n' for item in lines]
        # join the list back into a string and return it
        return ''.join(lines)

tkt=ATTelnetController('172.33.44.156','root','23',None)
tkt.connect()
tkt.run_command('ls',10)
tkt.disconnect()
'''
#??????????????????????
   


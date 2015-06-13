
'Exercise 8: get interface infomation'

import sys
import time
import paramiko
from E7 import get_net_info
from E7_window import get_net_info_win


def get_interfaces(ip_address, platform):
    '''
    get info interfaces: support platform window, linux
    '''
    count = 0
    re_try = 3
    username='temp'
    password='123'

    while True:
        print "Trying to connect to %s (%i/3)" % (ip_address, count)
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip_address,
                                username=username, password=password)
            print "Connected to %s" % ip_address
            break
        except paramiko.AuthenticationException:
            print "Authentication failed when connecting to %s" % ip_address
            sys.exit(1)
        except Exception as e:
            print e
            count += 1
            time.sleep(2)

        if count == re_try:
            print "Could not connect to %s" % ip_address
            sys.exit(1)

    if platform == 'window':
        stdin, stdout, stderr = ssh.exec_command("ipconfig /all")
    else:
        stdin, stdout, stderr = ssh.exec_command("ifconfig")

    ip_config = ''
    while not stdout.channel.exit_status_ready():
        while stdout.channel.recv_ready():
            ip_config += stdout.channel.recv(1024)

    print "Command done, closing SSH connection"
    ssh.close()

    if platform == 'linux':
        return get_net_info(ip_config)
    elif platform == 'window':
        return get_net_info_win(ip_config)
    else:
        return get_net_info_mac(ip_config)

'''
Only support linux, window
not yet support MAC platform
'''
# print get_interfaces('localhost', 'linux')
print get_interfaces('localhost', 'window')

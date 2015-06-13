'''
Created on May 15, 2015

@author: KHIEM
'''
# Exercise 1
#===============================================================================
# import copy
# d = dict(
#           x = 1,
#           y = dict(y1 = 'a', y2 = 'b')
#     )
# d2 = d
# #d2 = copy.deepcopy(d)
# d2['y'] = 1
# print d
#===============================================================================

#===============================================================================
# l=[2,3]
# k=l
# k[0]=5
# print l
#===============================================================================

# Exercise 2
#===============================================================================
# d = dict(x = 1, y = dict(y1 = 'a', y2 = 'b'))
# d2 = d.copy()
# d2['y']['y1'] = 'c'
# print d
#===============================================================================

# Exercise 3
#===============================================================================
# def getRadioId(radio):
#     if radio == 'g': return 1
#     elif radio == 'n': return 2
#     elif radio == 'a': return 3
#     elif radio == 'na': return 4
#     elif radio == 'ng': return 5
#     else:
#         return 'invalid'
# 
# print getRadioId('er')
#===============================================================================

'Exercise4:'
#===============================================================================
# def getTargetStation():
# while True:    
#     sta_11g = getTargetStation(sta_ips,"Pick an 11g wireless station: ")
#     sta_11n = getTargetStation(sta_ips, "Pick an 11n 2.4G wireless station: ")
#     sta_11n50 = getTargetStation(sta_ips, "Pick an 11n 5.0G wireless station: ")
#     sta_11a = getTargetStation(sta_ips, "Pick an 11a wireless station: ")
#     
#     if (sta_11g or sta_11n or sta_11n50 or sta_11a): break
#     
#     print "Pick at least one station as your target"
#===============================================================================

'Exercise:5,6'
#===============================================================================
# input = """
#         Physical Address. . . . . . . . . : 00-0C-F1-65-5B-70
#         IP Address. . . . . . . . . . . . : 192.168.1.100
#         Subnet Mask . . . . . . . . . . . : 255.255.255.0
#         DHCP Server . . . . . . . . . . . : 192.168.1.1
#         DNS Servers . . . . . . . . . . . : 192.168.1.1
#         Lease Obtained. . . . . . . . . . : Thursday, February 08, 2007 2:27:17PM
#         Lease Expires . . . . . . . . . . : Thursday, February 15, 2007 2:27:17PM
# """
# import time, re
# 
# def getNetInfo(input):
#     'get ip, netmask, mac, dns, lease_expires'
#     
#     info = dict(ip = getValue(input, 'IP Address'),
#             netmask = getValue(input, 'Subnet Mask'),
#             mac = getValue(input, 'Physical Address'),
#             dns = getValue(input, 'DNS Servers'),
#             lease_expires = getValue(input, 'Lease Expires'),
#             )
#     lease_expires = info['lease_expires']
#     lease_expires = re.findall('(.*,\s\d*)\s', lease_expires)[0]  # match *, 2007 
#     lease_expires = time.strptime(lease_expires, "%A, %B %d, %Y")
#     
#     info['lease_expires'] = time.strftime("%Y/%m/%d", lease_expires)
#     
#     return info
#   
# def getValue(input, name):
#     'return value of name from input'    
#       
#     tmp_line = input.split('\n')
#     for i in tmp_line:
#         if i.find(name) != -1:
#             return re.findall('.* . . :\s(\S.*)',i)[0]
#       
# output = getNetInfo(input)
# print output
#===============================================================================

'Exercise: 7'
input = """
eth0      Link encap:Ethernet  HWaddr 00:50:56:b0:db:66  
          inet addr:10.10.24.65  Bcast:10.10.25.255  Mask:255.255.254.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:71776 errors:0 dropped:0 overruns:0 frame:0
          TX packets:28345 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:6745598 (6.7 MB)  TX bytes:1938996 (1.9 MB)
lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:84 errors:0 dropped:0 overruns:0 frame:0
          TX packets:84 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:10122 (10.1 KB)  TX bytes:10122 (10.1 KB)
lo2        Link encap:Local Loopback
          inet addr:127.0.0.2  Mask:255.0.0.0
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:84 errors:0 dropped:0 overruns:0 frame:0
          TX packets:84 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:10122 (10.1 KB)  TX bytes:10122 (10.2 KB)

"""
 
import re
 
def getNetInfo(input):
    'get info for eth0, lo ...'
     
    tmp_input = input
    card_value = [] # list value of card_name 
    card_type = re.findall('(^\S+)\s', input, re.MULTILINE)
        
    for i in range(len(card_type) - 1):
        tmp_input = tmp_input.split(card_type[i + 1] + ' ') # card_type[i + 1] + ' ' make lo different from lo2
        card_value.append(tmp_input[0])
        tmp_split = tmp_input[1]
        tmp_input = tmp_split
        
    card_value.append(tmp_split)
    tmp_ouput = {}
    
    for i in range(len(card_type)):
        tmp_ouput.update ({ card_type[i] : getValue(card_value[i]) })
    
    return tmp_ouput
 
def getValue(input_type):
    'get value from type: eth, lo'
     
    mac = '' 
    broadcast = ''
    type = 'lo'
    status = 'UP'
    ip=re.findall('inet addr:(\S+)\s', input_type)[0]
    netmask=re.findall('Mask:(\S+)\s', input_type)[0]
     
    if input_type.find('HWaddr') != -1:
        mac = re.findall('HWaddr\s(\S+)\s', input_type)[0]
     
    if re.search('Bcast:(\S+)\s', input_type):
        broadcast = re.findall('Bcast:(\S+)\s', input_type)[0]
     
    if input_type.find('Ethernet') != -1:
        type = 'eth'
     
    if input_type.find('UP') == -1:
        status = 'DOWN'        
     
    return dict(ip=ip,
            netmask=netmask,
            broadcast=broadcast,
            mac=mac,
            type=type,
            status=status,
            )
     
output = getNetInfo(input)
print output
 
 
#===============================================================================
# 'E4'
# def getTargetStation(dd, gg):
#     print 'get'
#     return None
# sta_ips =0
# count = 0
# while True:
#     sta_11g = getTargetStation(sta_ips,"Pick an 11g wireless station: ")
#     sta_11n = getTargetStation(sta_ips, "Pick an 11n 2.4G wireless station: ")
#     sta_11n50 = getTargetStation(sta_ips, "Pick an 11n 5.0G wireless station: ")
#     sta_11a = getTargetStation(sta_ips, "Pick an 11a wireless station: ")
#  
#     if (sta_11g or sta_11n or sta_11n50 or sta_11a): break
#     else:
#         print "Pick at least one station as your target"
#         count +=1
#         if count == 10:
#             print 'Retry 10 times failed'
#             break
#===============================================================================

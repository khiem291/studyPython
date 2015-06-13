'Exercise 7, version window'

import time
import re

input = """
 Windows IP Configuration

   Host Name . . . . . . . . . . . . : PEGASUS
   Primary Dns Suffix  . . . . . . . :
   Node Type . . . . . . . . . . . . : Hybrid
   IP Routing Enabled. . . . . . . . : No
   WINS Proxy Enabled. . . . . . . . : No
   DNS Suffix Search List. . . . . . : nhaude
   System Quarantine State . . . . . : Not Restricted


Ethernet adapter Local Area Connection 3:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : TAP-Windows Adapter V9
   Physical Address. . . . . . . . . : 00-FF-6E-63-04-60
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   Link-local IPv6 Address . . . . . : fe80::7104:633c:2c7f:6c66%28(Preferre
   IPv4 Address. . . . . . . . . . . : 10.1.15.14(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.252
   Lease Obtained. . . . . . . . . . : 09 June, 2015 9:06:46 PM
   Lease Expires . . . . . . . . . . : 08 June, 2016 9:06:46 PM
   Default Gateway . . . . . . . . . :
   DHCP Server . . . . . . . . . . . : 10.1.15.13
   DHCPv6 IAID . . . . . . . . . . . : 637599598
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-1A-65-84-11-64-66-B3-00-C

   DNS Servers . . . . . . . . . . . : fec0:0:0:ffff::1%1
                                       fec0:0:0:ffff::2%1
                                       fec0:0:0:ffff::3%1
   NetBIOS over Tcpip. . . . . . . . : Enabled

Ethernet adapter Bluetooth Network Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Bluetooth Device (Personal Area Netwo
   Physical Address. . . . . . . . . : 00-27-13-98-0A-A7
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Ethernet adapter Local Area Connection:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Realtek PCIe GBE Family Controller
   Physical Address. . . . . . . . . : 64-66-B3-00-C0-2C
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes

Wireless LAN adapter Wireless Network Connection:

   Connection-specific DNS Suffix  . : nhaude
   Description . . . . . . . . . . . : Qualcomm Atheros AR9285 Wireless NetwAdapter
   Physical Address. . . . . . . . . : 00-17-C4-E3-00-77
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.1.99(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : 09 June, 2015 9:33:50 PM
   Lease Expires . . . . . . . . . . : 17 July, 2151 6:33:56 AM
   Default Gateway . . . . . . . . . : 192.168.1.1
   DHCP Server . . . . . . . . . . . : 192.168.1.1
   DNS Servers . . . . . . . . . . . : 8.8.8.8
   NetBIOS over Tcpip. . . . . . . . : Enabled

Tunnel adapter isatap.nhaude:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0
   DHCP Enabled. . . . . . . . . . . : No
   Autoconfiguration Enabled . . . . : Yes

"""


def get_net_info_win(input):
    'get ip, netmask, mac, dns, lease_expires'

    tmp_input = input
    card_value = []  # list card_name
    card_type = re.findall('(^\S.*):', input, re.M)

    if len(card_type) == 0:
            return {}
    elif len(card_type) == 1:
            card_value.append(tmp_input)
    else:
            for i in range(len(card_type) - 1):
                tmp_input = tmp_input.split(card_type[i + 1])
                card_value.append(tmp_input[0])
                tmp_split = tmp_input[1]
                tmp_input = tmp_split

            card_value.append(tmp_split)
    tmp_ouput = {}
    for i in range(len(card_type)):
        tmp_ouput.update({card_type[i]: get_detail(card_value[i])})

    return tmp_ouput


def get_detail(input_card_value):

    info = dict(ip=get_value(input_card_value, 'IPv4 Address'),
                        netmask=get_value(input_card_value, 'Subnet Mask'),
                        mac=get_value(input_card_value, 'Physical Address'),
                        dns=get_value(input_card_value, 'DNS Servers'),
                        lease_expires=get_value(input_card_value, 'Lease Expires'),
                        )
    return info


def get_value(input, name):
    'return value of name from input'

    if input.find(name) == -1:
        return None

    tmp_line = input.split('\n')
    for i in tmp_line:
        if i.find(name) != -1:
            return re.findall('.* . . :\s(\S.*)', i)[0]

# output = get_net_info_win(input)
# print output
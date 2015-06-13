'Exercise: 7'

import re

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

"""

def get_net_info(input):
    'get info for eth0, lo ...'

    tmp_input = input
    card_value = []  # list card_name
    card_type = re.findall('(^\S+)\s', input, re.MULTILINE)

    if len(card_type) == 0:
            return {}
    elif len(card_type) == 1:
            card_value.append(tmp_input)
    else:
            for i in range(len(card_type) - 1):
                tmp_input = tmp_input.split(card_type[i + 1] + ' ')  # card_type[i + 1] + ' ' make lo different from lo2
                card_value.append(tmp_input[0])
                tmp_split = tmp_input[1]
                tmp_input = tmp_split

            card_value.append(tmp_split)
    tmp_ouput = {}
    for i in range(len(card_type)):
        tmp_ouput.update({card_type[i]: get_value(card_value[i])})

    return tmp_ouput


def get_value(input_type):
    'get value from type: eth, lo'

    mac = ''
    broadcast = ''
    type = 'lo'
    status = 'UP'
    ip = re.findall('inet addr:(\S+)\s', input_type)[0]
    netmask = re.findall('Mask:(\S+)\s', input_type)[0]

    if input_type.find('HWaddr') != -1:
        mac = re.findall('HWaddr\s(\S+)\s', input_type)[0]

    if re.search('Bcast:', input_type):
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

# output = get_net_info(input)
# print output
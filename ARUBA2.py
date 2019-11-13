#!/usr/bin/env python

from netmiko import ConnectHandler 
from datetime import datetime
import sys
import getpass
import re
 
 #######################################################################
 # Warnings module needed to be imported to solve a connection mode    #
 # deprecated warrning that I was geting when trying to connect to     #
 # the juniper switches                                                #
 #######################################################################

import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

########################################################################

username = 'dsantos'
password = getpass.getpass()

########################################################################

#list_of_devices = ['10.23.4.54',
#                   '10.23.4.55',
#                   '10.23.4.59',
#                  ]
#list_of_devices = open('ARUBA-DEVICES.txt','r')

with open('ARUBA-DEVICES.txt') as file: # This opens the text file with the name ARUBA-DEVICES.txt in csv format (IP,hostname)
    list_of_devices = file.read().splitlines() # The file is loaded into the "list_of_devices" variable and splited into lines

#######################################################################

for line in list_of_devices:
  host_to_create = line.split(',') #this will create a list by spliting the line into two elements, considering the coma as delimiter for the strip.
  octects = host_to_create[0].split('.')
  
  print('Establishing connection to ' + host_to_create[1])
  
  start_time = datetime.now()

  net_connect = ConnectHandler(device_type='hp_procurve', ip=host_to_create[0], username=username, password=password, global_delay_factor=3.5)
  
  print('Connected to ' + host_to_create[1])
  
  net_connect.send_command('\n')
  net_connect.send_command('conf t', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.' + octects[1] + '.221.0 255.255.255.0 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.' + octects[1] + '.96.0 255.255.255.0 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.160.96.0 255.255.252.0 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.162.96.0 255.255.252.0 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.166.96.0 255.255.252.0 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.180.5.178 255.255.255.255 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.180.8.240 255.255.255.240 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.180.12.14 255.255.255.248 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.180.19.2 255.255.255.255 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.190.96.0 255.255.254.0 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.190.80.0 255.255.240.0 access-method ssh', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.' + octects[1] + '.221.0 255.255.255.0 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.' + octects[1] + '.4.0 255.255.255.0 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.' + octects[1] + '.4.10 255.255.255.0 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.160.96.0 255.255.252.0 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.166.92.0 255.255.252.0 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.166.96.0 255.255.252.0 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.180.5.176 255.255.255.240 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.180.8.240 255.255.255.240 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.180.12.14 255.255.255.248 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 10.180.19.2 255.255.255.255 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 185.85.222.99 255.255.255.255 access-method snmp', expect_string=r"#")
  net_connect.send_command('ip authorized-managers 185.85.222.100 255.255.255.255 access-method snmp', expect_string=r"#")
  net_connect.send_command('snmp-server community "public" unrestricted', expect_string=r"#")
  net_connect.send_command('snmp-server community "zalando_read" unrestricted', expect_string=r"#")
  net_connect.send_command('snmp-server host 10.180.5.178 community "zalando_read" trap-level all', expect_string=r"#")
  net_connect.send_command('snmp-server host 185.85.222.99 community "zalando_read" trap-level all', expect_string=r"#")
  net_connect.send_command('snmp-server host 185.85.222.100 community "zalando_read" trap-level all', expect_string=r"#")
  net_connect.send_command('snmp-server host 10.180.8.240 community "zalando_read" trap-level all', expect_string=r"#")
  net_connect.send_command('snmp-server host 10.180.12.14 community "zalando_read" trap-level all', expect_string=r"#")
  net_connect.send_command('snmp-server host 10.180.12.15 community "zalando_read" trap-level all', expect_string=r"#")
  net_connect.send_command('snmp-server host 10.180.12.17 community "zalando_read" trap-level all', expect_string=r"#")
  net_connect.send_command('save', expect_string=r"#")
  end_time = datetime.now()
  print('\nTotal time: {}'.format(end_time - start_time))
  print('Configuration successfully applied to the device ' + host_to_create[1] +'\n\n' + '#' * 60)
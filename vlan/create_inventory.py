import configparser
config = configparser.ConfigParser()

config.add_section('switches')

config.set('switches','Local_Switch general_settings','Local_Switch,512Mb,1,/usr/bin/qemu-system-x86_64 (v4.2.1),CD/DVD-ROM or HDD,Power off the VM,telnet')
config.set('switches','Local_Switch network_settings','13,0c:c0:5e:66:00:00,Realtek 8139 Ethernet (rtl8139),true')
config.set('switches','Local_Switch ansible_host','10.10.1.24')

config.set('switches','User_Network general_settings','User_Network,512Mb,1,/usr/bin/qemu-system-x86_64 (v4.2.1),CD/DVD-ROM or HDD,Power off the VM,telnet')
config.set('switches','User_Network network_settings','13,0c:e0:f2:0b:00:00,Realtek 8139 Ethernet (rtl8139),true')
config.set('switches','User_Network ansible_host','10.10.1.22')

config.set('switches','ACCT_Network general_settings','ACCT_Network,512Mb,1,/usr/bin/qemu-system-x86_64 (v4.2.1),CD/DVD-ROM or HDD,Power off the VM,telnet')
config.set('switches','ACCT_Network network_settings','13,0c:40:34:07:00:00,Realtek 8139 Ethernet (rtl8139),true')
config.set('switches','ACCT_Network ansible_host','10.10.1.32')

config.set('switches','MGMT_Network general_settings','MGMT_Network,512Mb,1,/usr/bin/qemu-system-x86_64 (v4.2.1),CD/DVD-ROM or HDD,Power off the VM,telnet')
config.set('switches','MGMT_Network network_settings','13,0c:cc:78:5d:00:00,Realtek 8139 Ethernet (rtl8139),true')
config.set('switches','MGMT_Network ansible_host','10.10.1.31')

config.set('switches','IT_Network general_settings','IT_Network,512Mb,1,/usr/bin/qemu-system-x86_64 (v4.2.1),CD/DVD-ROM or HDD,Power off the VM,telnet')
config.set('switches','IT_Network network_settings','13,0c:1c:b2:85:00:00,Realtek 8139 Ethernet (rtl8139),true')
config.set('switches','IT_Network ansible_host','10.10.1.30')

config.add_section('switches:vars')
config.set('switches:vars','ansible_user','ssh_user')
config.set('switches:vars','ansible_ssh_pass','P@ssw0rd')
config.set('switches:vars','ansible_connection','network_cli')
config.set('switches:vars','ansible_network_os','exos')

with open('inventory.ini','w') as f:
	config.write(f,space_around_delimiters=False)

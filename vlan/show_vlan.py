import configparser
import netmiko
from netmiko import ConnectHandler

config = configparser.ConfigParser()
config.read('inventory.ini')

#local_switch_ip = config.get('switches','local_switch ansible_host')
user_network_ip = config.get('switches','user_network ansible_host')
acct_network_ip = config.get('switches','acct_network ansible_host')
mgmt_network_ip = config.get('switches','mgmt_network ansible_host')
it_network_ip = config.get('switches','it_network ansible_host')

user = 'ssh_user'

key = '/home/student/.ssh/id_rsa'

user_network = {
	'device_type':'extreme',
	'host':user_network_ip,
	'username':user,
	'use_keys':True,
	'key_file':key
}

acct_network = {
	'device_type':'extreme',
	'host':acct_network_ip,
	'username':user,
	'use_keys':True,
	'key_file':key
}

mgmt_network = {
	'device_type':'extreme',
	'host':mgmt_network_ip,
	'username':user,
	'use_keys':True,
	'key_file':key
}

it_network = {
	'device_type':'extreme',
	'host':it_network_ip,
	'username':user,
	'use_keys':True,
	'key_file':key
}

with ConnectHandler(**user_network) as ssh:
	output = ssh.send_command('show vlan',use_textfsm=True)
	print("**********************************")
	print("********** USER NETWORK **********")
	print(output)

with ConnectHandler(**acct_network) as ssh:
	output = ssh.send_command('show vlan',use_textfsm=True)
	print("**********************************")
	print("********** ACCT_NETWORK **********")
	print(output)

with ConnectHandler(**mgmt_network) as ssh:
	output = ssh.send_command('show vlan',use_textfsm=True)
	print("**********************************")
	print("********** MGMT_NETWORK **********")
	print(output)

with ConnectHandler(**it_network) as ssh:
	output = ssh.send_command('show vlan',use_textfsm=True)
	print("**********************************")
	print("**********  IT_NETWORK  **********")
	print(output)

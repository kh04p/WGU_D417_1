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
	output = ssh.send_command('create vlan USER_NETWORK description User_Network tag 100',use_textfsm=True)
	print("**********************************")
	print("********** USER NETWORK **********")
	print("Successfully sent VLAN creation command.")

with ConnectHandler(**acct_network) as ssh:
	output = ssh.send_command('create vlan ACCT_NETWORK description Acct_Network tag 200',use_textfsm=True)
	print("**********************************")
	print("********** ACCT_NETWORK **********")
	print("Successfully sent VLAN creation command.")

with ConnectHandler(**mgmt_network) as ssh:
	output = ssh.send_command('create vlan MGMT_NETWORK description Mgmt_Network tag 300',use_textfsm=True)
	print("**********************************")
	print("********** MGMT_NETWORK **********")
	print("Successfully sent VLAN creation command.")

with ConnectHandler(**it_network) as ssh:
	output = ssh.send_command('create vlan IT_NETWORK description IT_Network tag 400',use_textfsm=True)
	print("**********************************")
	print("**********  IT_NETWORK  **********")
	print("Successfully sent VLAN creation command.")

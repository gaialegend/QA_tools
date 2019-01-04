#-*- coding:utf-8 -*-

import paramiko
import re
import json
import os
ip = '109.244.1.51'
port = 22

_ip = '109.244.1.50'


ip_dic = {'server_1':'109.244.1.50','server_2':'109.244.1.51','server_800':'139.199.165.219','inter_server':'115.182.192.229'}
filename = 'bin.zip'

def restartserver(server):
	global ip
	global port
	global _ip
	global ip_dic
	#print ip+str(port)
	command_dic = {'server_1':'cd server_1/bin;ls;./service restart','server_2':'cd server_2/bin;ls;./service restart','inter_server':'cd Inter_server;./service restart'}
	# if platform == '230' or platform != '229':
	# 	print '230'
	# 	__ip = _ip
	# 	command = 'cd server/bin;ls;./service restart'
	# else:
	# 	print '229'
	# 	__ip = ip
	# 	command = 'cd server_2/bin;ls;./service restart'
	#path = 'server_2/bin'
	command = command_dic[server]
	trans = paramiko.Transport((ip_dic[server],port))
	trans.connect(username='test1',password='Pass@9966')
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	print command
	stdin,stdout,stderr = ssh.exec_command(command)
	#print stdout.read().decode(s)
	#stdin, stdout, stderr = ssh.exec_command('./server start')
	#print 'hello'
	if stderr == None:
		print 'true'
		result = stderr.read().decode('utf-8')
		print type(result)
		print 'result = ' + str(result)
	else:
		result = stdout.read().decode()
		print type(result)
		print result
	trans.close()
	return result

def get_serverstatus(server):
	server_dic = {}
	global ip_dic
	global port
	command_dic = {'server_1':'cd server_1/bin;ls;./service status','server_2':'cd server_2/bin;ls;./service status'}
	command = command_dic[server]
	trans = paramiko.Transport((ip_dic[server],port))
	trans.connect(username='test1',password='Pass@9966')
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	stdin,stdout,stderr = ssh.exec_command(command)
	if stderr == None:
		result = stderr.read().decode('utf-8')
	else:
		result = stdout.read().decode('utf-8')
		#print str(result).split('\x1b')
		for x in str(result).split('\x1b'):
			rr = re.compile(r'\w*_server\w*')
			nu = re.compile('[0-9]+')
			#print type(rr.findall(x))
			#print rr.findall(x)
			if len(rr.findall(x)) != 0:
				print nu.findall(x)
				if len(nu.findall(x)) >= 2 and len(nu.findall(x)[-1])>2:
					server_dic[rr.findall(x)[0].strip('32m')] = nu.findall(x)[-1]
				else:
					li = nu.findall(x)
					li.append('stoped')
					print li
					server_dic[rr.findall(x)[0].strip('32m')] = li[-1]

				# print rr.findall(x)[0].strip('32m')
				# print nu.findall(x)[-1]
	print server_dic
	trans.close()
	return server_dic

def get_serverstatus_new(server):
	global ip_dic
	global port
	command = 'python check_pid.py'
	trans = paramiko.Transport((ip_dic[server],port))
	trans.connect(username='test1',password='Pass@9966')
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	stdin,stdout,stderr = ssh.exec_command(command)
	stdout_r=eval(stdout.read())
	#print stdout_r.keys()
	return stdout_r
	#print type(eval(stdout_r))


def server_switch(server,switch):
	stop_command = {'server_1':'cd server_1/bin;ls;./service stop','server_2':'cd server_2/bin;ls;./service stop'}
	start_command = {'server_1':'cd server_1/bin;ls;./service restart','server_2':'cd server_2/bin;ls;./service restart'}
	switch_dic = {'stop':stop_command,'start':start_command}
	command = switch_dic[switch]
	command = command[server]
	# command = command_dic[server]
	trans = paramiko.Transport((ip_dic[server],port))
	trans.connect(username='test1',password='Pass@9966')
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	stdin,stdout,stderr = ssh.exec_command(command)	
	if stderr == None:
		result = stderr.read().decode('utf-8')
	else:
		result = stdout.read().decode('utf-8')
	return result


def restartserver_():
	global _ip
	global port
	trans = paramiko.Transport((ip,port))
	trans.connect(username='test1',password='Pass@9966')
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	command = 'cd server/bin;ls;./service restart'
	stdin,stdout,stderr = ssh.exec_command(command)
	result = stdout.read().decode()
	return result

def time(server):
	global ip
	global _ip
	global port
	global ip_dic
	trans = paramiko.Transport((ip_dic[server],port))
	trans.connect(username='test1',password='Pass@9966')
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	command = 'date'
	stdin,stdout,stderr = ssh.exec_command(command)
	result = stdout.read().decode()
	#print result
	trans.close()
	return result

def time_switch(time, server):
	global ip
	global port
	global _ip
	global ip_dic
	trans = paramiko.Transport((ip_dic[server],port))
	trans.connect(username='test1',password='Pass@9966')
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	command = 'sudo date -s ' + str(time)
	print command
	stdin,stdout,stderr = ssh.exec_command(command,get_pty=True)
	result = stdout.read().decode()
	if stderr != None:
		result_r = stderr.read().decode()
		print result_r
	else:
		print result
	print '------------------------------------------------'
	trans.close()
	return result

def server_update(filename_,server):
	global ip_dic
	global port
	trans = paramiko.Transport((ip_dic[server],port))
	trans.connect(username='test1',password='Pass@9966')
	ssh = paramiko.SSHClient()
	ssh._transport = trans
	command_unzip = 'yes|unzip ' +  filename_
	update_comand = {'server_1':'./update','server_2':'./update_2','inter_server':'./update_Is'}
	sdin,stdout,stderr = ssh.exec_command(command_unzip)
	stdin_2,stdout_2,stderr_2 = ssh.exec_command(update_comand[server])
	if stderr_2 == None:

		result = stdout_2.read().decode()
	else:
		result = stderr_2.read().decode()
		if 'No such file or directory' in result:
			stdin_3,stdout_3,stderr_3 = ssh.exec_command('ls')
			print stdout_3.read().decode()
			print stderr_3.read().decode()
	# if stderr == None:
	# 	print stderr
	# 	result = stdout.read().decode()
	# 	trans.close()
	# else:
	# 	result = stderr.read().decode()
	return result	

def server_update_new(filename_,server):
	global ip_dic
	global port
	#print filename_
	print os.getcwd()
	dir_path_ = os.path.pardir
	#file_path = os.path.abspath(os.path.join(os.getcwd(),dir_path_,))+'\\upload_file'
	#print file_path
	file_path = os.getcwd()+'\\upload_file'
	trans = paramiko.Transport((ip_dic[server],port))
	trans.connect(username='test1',password='Pass@9966')
	sftp = paramiko.SFTPClient.from_transport(trans)
	#print file_path
	path_name = file_path+'\\'+filename_
	print path_name
	sftp.put(path_name,'/data1/test1/'+filename_)
	return filename_

def reset_time(server):
	add = {'server_1':'cd server_1/bin','server_2':'cd server_2/bin','inter_server':'cd Inter_server/bin'}
	comm = {'stop':'./service stop','start':'./service restart','reset_time':'sudo ntpdate 61.172.254.29'}
	back = 'cd ../..'
	global ip_dic
	global port
	trans = paramiko.Transport((ip_dic[server],port))
	trans.connect(username='test1',password='Pass@9966')
	ssh._transport= trans
	if server == 'server_2' or server == 'inter_server':
		for x in ['server_2','inter_server']:
			for _comm in [add[x],comm['stop'],comm['reset_time'],comm['start']]:
				try:
					stdin,stdout,stderr = ssh.exec_command(_comm)
				except:
					stdout = 'Error'
					break
	else:
		for x in ['server_1']:
			for _comm in [add[x],comm['stop'],comm['reset_time'],comm['start']]:
				try:
					stdin,stdout,stderr = ssh.exec_command()
				except:
					pass

	return 






if __name__ == '__main__':
	server_update_new('bin_branch_ob3.zip','server_1')
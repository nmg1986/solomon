#!/usr/bin/python
import os
import commands
import subprocess

SCRIPT_DIR="/etc/solomon/script.d"

def strcmp(str1,str2):
	if str1 == str2 :
		return True
	else:
		return False
def strcat(str1,*strn):
	for arg in strn:
		str1 += arg
	return str1	

def is_exist(file):
	return os.path.isfile(file)

def is_executable(file):
	return os.access(file,os.X_OK)	

def absolute_path(command):
	path=os.path.join(SCRIPT_DIR,command)
	return path 

def send_email(section):
	pass
def service_failover():
	pass

def run(command):
	status,output=commands.getstatusoutput(command)
	if status == 0:
		return True
	else:
		return False

def get_command(basename):
	dirname=get_script_dir()
	path=os.path.join(dirname,basename)	
	return path 

def service_failover():
	fnull=open(os.devnull,'w')
	if is_exist("/etc/init.d/heartbeat") and is_executable("/etc/init.d/heartbeat"):
		subprocess.call(["/etc/init.d/heartbeat","restart"])
	else:
		pass	
	fnull.close()

def set_pid(pidfile):
	
	pid=os.getpid()
	file(pidfile,'w').write(str(pid)+'\n')
	#fd=open(file,'w')
	#fd.write(str(pid)+'\n')
	#fd.close()

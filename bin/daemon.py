#!/usr/bin/python

import sys,os

def initDaemon():
	try:
		pid = os.fork()
		if pid > 0:
			sys.exit(0)
	except OSError,e:
		sys.exit(1)
	
	os.chdir("/")
	os.setsid()
	os.umask(0)

	try:
		pid = os.fork()
		if pid > 0:
			sys.exit(0)
	except OSError,e:
		sys.exit(1)

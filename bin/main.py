#!/usr/bin/python

import functions
import multiprocessing
import time

def initparser(file):

	import ConfigParser
	parser=ConfigParser.SafeConfigParser()
	parser.read(file)
	return parser

def get_enabled_sections(parser,sections):
	check_list=[]
	for item in sections:
		if parser.has_option(item,"enabled"):
			if functions.strcmp(parser.get(item,"enabled"),"true"):
				check_list.append(item) 		
	return check_list 

def resource_check(section,*args):
	resource_name=section
	check_command=args[0]
	check_interval=args[1]
	retry_interval=args[2]
	retry_times=args[3]
	event_handler=args[4]
	
	_retry_times=0
	while True:
		status=functions.run(check_command)
		if functions.strcmp(status,"OK"):
			logger.info(functions.strcat(resource_name,":","resource state is ok..."))
		elif functions.strcmp(status,"WARNING"):
			logger.warning(functions.strcat(resource_name,":","resource state is warning...")
			if _retry_times < retry_times : 
				logger.info(functions.strcat("try check after",retry_interval,"seconds..."))
				_retry_times = _retry_times + 1 
				time.sleep(float(retry_interval))
				continue
			else:
				logger.critical(functions.strcat(resource_name,":","resource seems has gone-away!!!")
				logger.info(functions.strcat(resource_name,":","tells event handler to deal with this situation...")
				functions.run(event_handler)
	        time.sleep(float(check_interval))
	
    

def do_check(section,*args):
        task_name="check-{}".format(section)
	task=mutilprocessing.Process(name=task_name,target=resource_check,args=(section,args)
        task.start()
        task.join()
	


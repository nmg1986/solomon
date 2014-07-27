#!/usr/bin/python

import functions

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

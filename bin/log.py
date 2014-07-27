#!/usr/bin/env python

def initlog(file):
	import logging 
	logger=logging.getLogger()
	hdlr=logging.FileHandler(file)
	formatter=logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr)
	logger.setLevel(logging.NOTSET)

	return logger

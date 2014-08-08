#!/usr/bin/python

import parser

parser=parser.initparser("/etc/solomon/conf.d/global.conf")

pid=parser.get("global","pid")
log=parser.get("global","log")

check_interval=parser.get("global","check_interval")
retry_interval=parser.get("global","retry_interval")
retry_times=parser.get("global","retry_times")
event_handler=parser.get("global","event_handler")

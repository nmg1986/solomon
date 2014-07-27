#!/usr/bin/python

import parser

parser=parser.initparser("/etc/solomon/conf.d/global.conf")

pid=parser.get("global","pid")
log=parser.get("global","log")
check_interval=parser.get("global","check_interval")

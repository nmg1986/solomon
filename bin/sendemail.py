#!/usr/bin/python
#-*- coding:utf-8 -*-

import parser
import subprocess
import sys
import smtplib
from   email.mime.text import MIMEText
import time

parser=parser.initparser("/etc/solomon/conf.d/email.conf")

enabled=parser.get("email","enabled")
description=parser.get("email","description")
smtp_server=parser.get("email","smtp_server")
smtp_port=parser.get("email","smtp_port")
sender=parser.get("email","sender")
send_to=parser.get("email","to").split(':')
send_cc=parser.get("email","cc").split(':')
user=parser.get("email","user")
password=parser.get("email","password")
HOST=parser.get("email","host")

DATE=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def send_email(name):
	str="%s is down" % name
	RESON=str.upper()
	content='''<html>
            <hr/>
	    <font>%s因故障发生主备机切换，请通知运维人员检查并修复故障。</font><br><br>
	    <font>告警详细信息如下：</font><br><br>
            <font color="red"><strong>告警主机 : %s </strong></font><br><br>
            <font color="red"><strong>告警原因 : %s </strong></font><br><br>
            <font color="red"><strong>告警时间 : %s </strong></font><br>
            <hr/>
         </html>''' % (description,HOST,RESON,DATE)
        #msg = MIMEText(content)
        msg = MIMEText(content,'html','utf-8')
        msg['subject'] = "%s%s" % (description,"双机故障告警")
        msg['from']= sender
        msg['to']= ','.join(send_to)
        msg['cc']=','.join(send_cc)
        try:
                s=smtplib.SMTP(smtp_server,smtp_port)
                s.login(user,password)
                s.sendmail(sender,send_to + send_cc,msg.as_string())
                s.quit()
                return True
        except Exception,e:
                return False

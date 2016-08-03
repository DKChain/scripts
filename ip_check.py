#! /bin/python
# -*- coding: utf-8 -*-

# author: DK Chain
# email: dkblack1996@gmail.com

import socket
import smtplib
from email.mime.text import MIMEText
import logging

def get_ip():
    #pcname = socket.getfqdn(socket.gethostname())
    #ipaddr = socket.gethostbyname(pcname)
    ipaddr = socket.gethostbyname(socket.gethostname())
    #print('Get ip success: %s' % ipaddr)
    return ipaddr

def send_email(old_ip, new_ip):
    sender = 'dk_black@163.com'
    pwd = '***'
    receiver = 'dkblack1996@gmail.com'

    message = MIMEText("Old IP: %s\nNew IP: %s" % (old_ip, new_ip))
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Marchine IP'
        
    try:
        smtpObj = smtplib.SMTP('smtp.163.com')
        smtpObj.login(sender, pwd)
        smtpObj.sendmail(sender, receiver, message.as_string())
        smtpObj.close()
        #print('Send success')
    except smtplib.SMTPException as e:
        #print(e)
        pass

def check():
    new_ip = None
    old_ip = None

    while True:
        #print('Getting IP address...')
        new_ip = get_ip()
        if new_ip == old_ip:
            continue
        send_email(old_ip, new_ip)
        old_ip = new_ip

if __name__ == '__main__':
    check()
    #print(get_ip())

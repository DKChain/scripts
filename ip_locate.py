#! /bin/python3
# -*- coding: utf-8 -*-

# author: DK
# email: dkblack1996@gmail.com

import urllib.request
import re
import sys

def usage():
    print("IP address locater.")
    print("Usage: python3 ip_locate.py IP_ADDRESS")

def locate(addr):
    page = urllib.request.urlopen('http://wap.ip138.com/ip.asp?ip=%s' % addr)
    content = page.read().decode('utf8')
    res = re.findall(r"<br/><b>查询结果：(.*)</b><br/>", content)
    return res[0]
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit()
    addr = sys.argv[1]
    print(locate(addr))

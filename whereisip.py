#--coding:utf-8---
#!usr/bin/python
import requests
def whereisip(ip):
    url="http://freeapi.ipip.net/"
    fullurl=url+ip
    s=requests.session()
    r=s.get(fullurl)
    print r.content
whereisip("112.1.31.143")

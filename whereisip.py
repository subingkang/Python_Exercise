#--coding:utf-8---
# Author: subk
# Time  : 2018/11/17 19:21
# Desc  :IP地址归属地查询，采用ipip.net免费数据


import requests
import time
import json
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}

s=requests.session()
with open(r'C:\Users\su\Desktop\a.txt') as f:
    for ip in f:
        # print ip
        url="http://freeapi.ipip.net/"+ip.strip('\n')
        con=s.get(url,headers=headers)
        ip_result= con.text
        if ip_result[0]=="[":
            print ip_result
            time.sleep(1)
        else:
            break

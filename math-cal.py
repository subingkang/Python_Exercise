# -*- coding: utf-8 -*-
import re
import requests

url = 'http://1.hacklist.sinaapp.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
'''用这个方法可以保持cookie,如果直接用requests.get()得不到结果'''
s=requests.session()
r = s.get(url)
con = r.content
math=re.findall(r'\d+.*\)',con)[0]
print math
print eval(math)
key = s.post(url, data={'v': eval(math)})
print key.content
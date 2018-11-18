#--coding:utf-8---
# Author: subk
# Time  : 2018/11/18 20:19
# Desc  : 替换某路径下所有txt文件中符合某条件的字符串，然后新建-new.txt文件替换


import re
import os
os.chdir(r"C:\Users\su\Desktop\aa")
dir_files=os.listdir(os.getcwd())

for file in dir_files:
    file_name_new= file[:-4]+"-new.txt"
    with open(file,"r") as f:
        for line in f.readlines():
            with open(file_name_new,'ab+') as f2:
                new_line=re.sub("login:((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))","login:k.k.k.k",line)
                f2.write(new_line.strip('\n'))
                f2.write('\n')

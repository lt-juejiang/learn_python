#!/user/local/bin/python3
# coding=utf-8

import re
# 切分字符串
print re.split(r'[\s\,]+', 'a,b , c   ,d')
print re.split(r'[\s\,\;]+', 'a,b , c;   ,d')

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
print m
print m.group(0)
print m.group(1)
print m.group(2)

t = '19:15:38'
m1 = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|\
[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print m1.group(0)
print m1.groups()
#贪婪匹配
print re.match(r'^(\d+)(0*)$', '1023000').groups()
print re.match(r'^(\d+?)(0*)$', '1023000').groups()
#编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345678').groups()
print re_telephone.match('021-234500').groups()


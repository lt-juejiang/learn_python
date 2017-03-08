#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# a = input('please input an e-mail:')
# # re_email = re.compile(r'^([\d\w_]+@[\d\w]+.\w{3})$')
# re_email = re.compile(r'^(\w+|\w+\.\w+)@(\w+\.\w+)$')
# if re_email.match(a):
#     print('success')
# else:
#     print('fail')




# #匹配邮件
# re_email = re.compile(r'^(\w+|\w+\.\w+)@(\w+\.\w+)$')
# email = 'bing@qq.com'
# s = re_email.match(email).groups()
# print(s)
#
# #分组提取，支持_-.符号
#
# email2 = 'ns-2332@163.net.cn'
# n = re.match(r'^([0-9a-z\_\-\.]+)@(\w+\.[a-z\.]+)$',email2)
# print(n.group(0))
# print(n.group(1))
# print(n.group(2))
#
# #匹配带名字的邮件
# email3 = '<Tom Paris> tom@voyager.org'
# name = re.match(r'^<(\w+\s?\w+)>\s([0-9a-z\_\-\.]+)@(\w+\.[a-z\.]+)$',email3)
# print(name.group(0))
# print(name.group(1))
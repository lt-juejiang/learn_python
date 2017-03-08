#!/user/bin/python
#coding=utf-8
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print('MD5:', md5.hexdigest())
md5.update('how to use md5 ii python hashlib?'.encode('utf-8'))
print('MD5:', md5.hexdigest())
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print('SHA1:', sha1.hexdigest())
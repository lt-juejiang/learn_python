__author__ = 'liuting'
import requests
import json

r = requests.get('http://www.baidu.com')
print(r.headers)
print(r.content)

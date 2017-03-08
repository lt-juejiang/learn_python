#!/user/bin/python
#coding=utf-8
############## 需要再学习 #######

import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.python.org/events/python-events')
soup = BeautifulSoup(page.content,'html')

count=0
for i in soup.select('h3[class="event-title"]'):
   count=count+1

for i in range(count):
   print('event-title:', soup.select('h3[class="event-title"]')[i].get_text())
   print('event-time:', soup.select('time')[i].get_text())
   print('event-location:', soup.select('span[class="event-location"]')[i].get_text())
   print('-'*20)
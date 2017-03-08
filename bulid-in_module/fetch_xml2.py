#!/user/bin/python
#coding=utf-8
from urllib import request
from bs4 import BeautifulSoup

def fetch_xml(url):
    req=request.Request(url)
    page=request.urlopen(req)
    f=page.read()
    soup=BeautifulSoup(f, 'html.parser')
    count=0
    for i in soup.select('div[class="D(ib) Va(m) W(1/4)"]'):
        count=count+1

    for j in range(count):
        print('星期:',soup.select('div[class="D(ib) Va(m) W(1/4)"]')[j].get_text())
        print('天气:',soup.select('span[class="D(ib) Va(m) W(1/4) Ta(c)"] > img')[j]['title'])
        a=soup.select('span[class="D(ib) Va(m) W(1/4) Ta(end)"]')[j].get_text()
        print('温度:','high:%sF, low:%sF'%(a[0:3],a[3:6]))
        print('-'*30)



fetch_xml('https://www.yahoo.com/news/weather/china/beijing/beijing-2151330')
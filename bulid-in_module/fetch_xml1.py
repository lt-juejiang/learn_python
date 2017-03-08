#!/user/bin/python
#coding=utf-8
from urllib import request, parse

def fetch_xml(url):
    req = request.Request(url)
    with request.urlopen(req) as response:
        print('Status: ', response.status, response.reason)
        return response.read().decode('utf-8')

if __name__=='__main__':
    print(fetch_xml('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22beijing%2C%20china%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeysw%2C%20scotland%22)%20and%20u%3D%27c%27%20&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'))
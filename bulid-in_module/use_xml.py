#!/user/bin/python
#coding=utf-8

from xml.parsers.expat import ParserCreate


data = r'''<query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2017-02-20T10:38:09Z" yahoo:lang="zh-CN">
<results>
<channel>
<yweather:units xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" distance="km" pressure="mb" speed="km/h" temperature="C"/>
<title>Yahoo! Weather - Beijing, Beijing, CN</title>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/
</link>
<description>Yahoo! Weather for Beijing, Beijing, CN</description>
<language>en-us</language>
<lastBuildDate>Mon, 20 Feb 2017 06:38 PM CST</lastBuildDate>
<ttl>60</ttl>
<yweather:location xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" city="Beijing" country="China" region=" Beijing"/>
<yweather:wind xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" chill="34" direction="115" speed="22.53"/>
<yweather:atmosphere xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" humidity="12" pressure="34778.23" rising="0" visibility="25.91"/>
<yweather:astronomy xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" sunrise="7:0 am" sunset="5:57 pm"/>
<image>
<title>Yahoo! Weather</title>
<width>142</width>
<height>18</height>
<link>http://weather.yahoo.com</link>
<url>
http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif
</url>
</image>
<item>
<title>
Conditions for Beijing, Beijing, CN at 05:00 PM CST
</title>
<geo:lat xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">39.90601</geo:lat>
<geo:long xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">116.387909</geo:long>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/
</link>
<pubDate>Mon, 20 Feb 2017 05:00 PM CST</pubDate>
<yweather:condition xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="Mon, 20 Feb 2017 05:00 PM CST" temp="3" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="20 Feb 2017" day="Mon" high="6" low="-3" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="5" date="21 Feb 2017" day="Tue" high="1" low="-2" text="Rain And Snow"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="30" date="22 Feb 2017" day="Wed" high="4" low="-3" text="Partly Cloudy"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="23 Feb 2017" day="Thu" high="7" low="-2" text="Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="24 Feb 2017" day="Fri" high="10" low="-5" text="Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="25 Feb 2017" day="Sat" high="11" low="-1" text="Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="26 Feb 2017" day="Sun" high="10" low="-2" text="Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="27 Feb 2017" day="Mon" high="11" low="-1" text="Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="34" date="28 Feb 2017" day="Tue" high="13" low="0" text="Mostly Sunny"/>
<yweather:forecast xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" code="32" date="01 Mar 2017" day="Wed" high="11" low="2" text="Sunny"/>
<description>
<![CDATA[<img src="http://l.yimg.com/a/i/us/we/52/30.gif"/> <BR /> <b>Current Conditions:</b> <BR />Partly Cloudy <BR /> <BR /> <b>Forecast:</b> <BR /> Mon - Partly Cloudy. High: 6Low: -3 <BR /> Tue - Rain And Snow. High: 1Low: -2 <BR /> Wed - Partly Cloudy. High: 4Low: -3 <BR /> Thu - Sunny. High: 7Low: -2 <BR /> Fri - Sunny. High: 10Low: -5 <BR /> <BR /> <a href="http://us.rd.yahoo.com/dailynews/rss/weather/Country__Country/*https://weather.yahoo.com/country/state/city-2151330/">Full Forecast at Yahoo! Weather</a> <BR /> <BR /> (provided by <a href="http://www.weather.com" >The Weather Channel</a>) <BR /> ]]>
</description>
<guid isPermaLink="false"/>
</item>
</channel>
</results>
</query>
<!--  total: 39  -->
<!--
 prod_sg3_1;paas.yql;queryyahooapiscomproductionsg3;7cbe3f63-f5d9-11e6-9341-9cb6547d9944
-->

'''

class WeatherSaxHandler(object):
    def __init__(self):
        self.weather_data={}

    def start_element(self,name,attr):
        if name==r'yweather:location':
            self.weather_data['city']=attr['city']
            self.weather_data['country']=attr['country']
        if name ==r'yweather:forecast':
            if attr['date']=="20 Feb 2017":
                self.weather_data['today'] = {'low': int(attr['low']), 'high': int(attr['high']), 'text': attr['text']}
            if attr['date']=='21 Feb 2017':
                self.weather_data['tomorrow'] = {'low': int(attr['low']), 'high': int(attr['high']), 'text': attr['text']}


def parser_weather(xml):
    weather_handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = weather_handler.start_element
    parser.Parse(xml)
    return weather_handler.weather_data


print(parser_weather(data))
print('end')
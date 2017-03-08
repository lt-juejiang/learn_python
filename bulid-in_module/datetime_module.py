#!/user/bin/python
#coding=utf-8
from datetime import datetime,timedelta,timezone
#获取当前时间
now = datetime.now()
print(now)
print(type(now))
#转换成时间戳
dt = datetime(2017, 2, 14, 12, 1, 0)
print(dt)
print(dt.timestamp())#python3版本才有

t = 1487044860.0
#时间戳转换成当前时间
print(datetime.fromtimestamp(t))
#时间戳转换成标准时间（UTC）
print(datetime.utcfromtimestamp(t))
#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
#datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print('**********************************')
#datetime加减
print(now)
print(now+timedelta(hours=3))
print(now+timedelta(days=1, hours=3))
print(now-timedelta(days=2))
print(now+timedelta(days=3)-timedelta(hours=2))
print('**********************************')
#时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
#不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换
tokyo_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

#!/user/bin/python
#coding=utf-8
from datetime import datetime, timedelta, timezone
import re
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    re_tz = re.compile(r'^UTC([+|-][0-9]{1,2}):00$')
    # tz_num = int(re.match(r'UTC([+|-][0-9]{1,2}):00',tz_str).group(1))
    tz = int(re_tz.match(tz_str).group(1))
    tz_utc = timezone(timedelta(hours=tz))
    dt_utc = dt.replace(tzinfo=tz_utc)
    return datetime.timestamp(dt_utc)


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
assert t1 == 1433121030.0
print('pass')
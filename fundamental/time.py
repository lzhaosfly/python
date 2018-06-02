import datetime
import time

t = datetime.time(5, 21, 1)  # 05:21:01
print(t.hour)  # 5

print(datetime.time.min)  # 00:00:00
print(datetime.time.max)  # 23:59:59.999999
print(datetime.time.resolution)  # 0:00:00.000001

today = datetime.date.today()  # 2018-06-01
print(today.year)  # 2018
print(today.month)  # 6
print(today.day)  # 1

d1 = datetime.date(2015, 3, 11)
d2 = d1.replace(year=1990)  # datetime.timedelta(9131)
print(d1 - d2)  # 9131 days, 0:00:00

now = datetime.datetime.now()  # 2018-06-01 17:42:29.531880
print(now.month)  # 6
print(now.hour)  # 17

print(datetime.datetime.fromtimestamp(
    1527900243.385782))  # 2018-06-01 17:44:03.385782

delta = datetime.timedelta(120)
print(now + delta)  # 2018-09-29 17:49:04.437254

print(now.timestamp())

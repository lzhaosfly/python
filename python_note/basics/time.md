# Time and DateTime

[datetime](https://docs.python.org/3/library/datetime.html)

# 1. time

```python
import time

print(time.time())  # seconds timestamp
```

# 2. date

```python
import datetime

today = datetime.date.today()  # 2018-06-01
print(today.year)  # 2018
print(today.month)  # 6
print(today.day)  # 1

d1 = datetime.date(2015, 3, 11)
d2 = d1.replace(year=1990)  # datetime.timedelta(9131)
print(d1 - d2)  # 9131 days, 0:00:00
```

# 3. datetime (see the timestamp and datetime convert)

```python
now = datetime.datetime.now()  # 2018-06-01 17:42:29.531880
print(now.month)  # 6
print(now.hour)  # 17

print(datetime.datetime.fromtimestamp(
    1527900243.385782))  # 2018-06-01 17:44:03.385782
print(now.timestamp()) # 2018-06-01 17:42:29.531880
```

## 4. timedelta

`datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`

```python
import datetime

now = datetime.datetime.now()  # 2018-06-01 17:42:29.531880
delta = datetime.timedelta(120)
print(now + delta)  # 2018-09-29 17:49:04.437254
```

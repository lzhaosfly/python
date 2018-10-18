# Time and DateTime

[datetime](https://docs.python.org/3/library/datetime.html)

# 0. format list

```
Commonly used format codes:

%Y  Year with century as a decimal number.
%m  Month as a decimal number [01,12].
%d  Day of the month as a decimal number [01,31].
%H  Hour (24-hour clock) as a decimal number [00,23].
%M  Minute as a decimal number [00,59].
%S  Second as a decimal number [00,61].
%z  Time zone offset from UTC.
%a  Locale's abbreviated weekday name.
%A  Locale's full weekday name.
%b  Locale's abbreviated month name.
%B  Locale's full month name.
%c  Locale's appropriate date and time representation.
%I  Hour (12-hour clock) as a decimal number [01,12].
%p  Locale's equivalent of either AM or PM.
```

# 1. time

```python
import time

timestamp = time.time()  # seconds timestamp
time.ctime(timestamp) # 'Tue Oct 16 19:31:19 2018'. Convert timestamp to str

utc_time_tuple = time.gmtime(timestamp) # return utc time tuple. 

# result: time.struct_time(tm_year=2018, tm_mon=10, tm_mday=17, tm_hour=2, tm_min=31, tm_sec=19, tm_wday=2, tm_yday=290, tm_isdst=0)

local_time_tuple = time.localtime(timestamp) # return local time tuple. 

#result: time.struct_time(tm_year=2018, tm_mon=10, tm_mday=16, tm_hour=19, tm_min=31, tm_sec=19, tm_wday=1, tm_yday=289, tm_isdst=1)

timestamp1 = time.mktime(local_time_tuple) # convert time tuple to time stamp
time.asctime(local_time_tuple) # 'Tue Oct 16 19:31:19 2018'. Convert time tuple to str

time_str = time.strftime("%Y-%m-%d %H:%M:%S"[, local_time_tuple]) # conver time tuple to your format
time_tuple = time.strptime(time_str, "%Y-%m-%d %H:%M:%S") # conver a timeStr to a time tuple

time.sleep(4) # sleep 4 seconds
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

datetime.date.today().strftime("%Y-%m-%d %H:%M:%S") # format date
```

# 3. datetime (see the timestamp and datetime convert)

```python
now = datetime.datetime.now()  # 2018-06-01 17:42:29.531880
print(now.month)  # 6
print(now.hour)  # 17

print(datetime.datetime.fromtimestamp(
    1527900243.385782))  # 2018-06-01 17:44:03.385782
print(now.timestamp()) # 2018-06-01 17:42:29.531880

datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # format datetime
datetime_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S") # str to datetime
```

## 4. timedelta

`datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)`

```python
import datetime

now = datetime.datetime.now()  # 2018-06-01 17:42:29.531880
delta = datetime.timedelta(120)
print(now + delta)  # 2018-09-29 17:49:04.437254

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds) # 11, 36548(10 hours, 9 min- utes, and 8 seconds, expressed in seconds), 0

delta.total_seconds() # 986948.0
str(delta) #' 11 days, 10:09:08'
```

## 5. calendar

```python
import calendar

print(calendar.month(2017, 7)) # print 2017/7 calendar
print(calendar.calendar(2017, 7)) # print 2017 calendar
calendar.isleap(2012) # check if it is leap year
```

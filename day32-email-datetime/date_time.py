import datetime as dt


now_time=dt.datetime.now()
year=now_time.year
month=now_time.month
day=now_time.day
hour=now_time.hour
minute=now_time.minute
second=now_time.second
week_day=now_time.weekday()
print(week_day)

my_birthday=dt.datetime(year=2004,month=9,day=5,hour=12)
print(my_birthday)
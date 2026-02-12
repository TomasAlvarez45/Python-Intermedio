### Dates ###

from datetime import datetime

now = datetime.now()
   
timestamp = now.timestamp()

print(timestamp)

year_2027 = datetime(2027, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date)
    print(date.timestamp())

print_date(year_2027)

from datetime import time

current_time = time(12, 34, 15)

current_time.hour

print(current_time.hour)
print(current_time.min)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date(2026, 2, 7)

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday)

current_date = date(current_date.year + 1, current_date.month + 1, current_date.day + 1)

print(current_date)


diff = year_2027 - now
print(diff)
diff = year_2027.date() - current_date
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 2, weeks = 10)
end_timedelta = timedelta(300, 100, 10, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)

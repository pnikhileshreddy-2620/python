import  datetime as dt
from datetime import datetime
import calendar

dt =dt.datetime
print(dt.now())
print(dt.now().today())
print(dt.today())
print(dt.now().date())
print(dt.now().year)
print(dt.now().weekday())

name =dt.now().weekday()

print(name)

day_name = calendar.day_name[name]
print(day_name)


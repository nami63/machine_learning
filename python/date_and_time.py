import datetime
now=datetime.datetime.now()
print(now)
current_date=datetime.date.today()
print(current_date)

from datetime import time

a=time(11,34,56)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)
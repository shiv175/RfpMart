from  datetime import datetime
from datetime import timedelta as td
now = datetime.now()
print(now)
for i in range(1,1000):
    print("Time")
    subtructvalue = datetime.now() - now
    totaltime = int(subtructvalue.total_seconds() * 1000)
    print(subtructvalue)
    print(totaltime)
"""print(subtructvalue)
print(x)
print(type(subtructvalue))
print(subtructvalue.strftime('%M:%S.%f'))"""
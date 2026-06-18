#1
import datetime

x = datetime.datetime.now()
x -= datetime.timedelta(days=5)
print (x)

#2
import datetime

x = datetime.datetime.now()
x -= datetime.timedelta(days=1)
print (f"Yesterday is {x}")

x = datetime.datetime.now()
print (f"Today is {x}")

x += datetime.timedelta(days=1)
print (f"Tomorrow is {x}")

#3
import datetime

x = datetime.datetime.now()
y = x.replace(microsecond=0)

print (y)

#4
import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days=5)

z = x - y

print (z.total_seconds())
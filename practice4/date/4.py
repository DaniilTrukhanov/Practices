import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days=5)

z = x - y

print (z.total_seconds())
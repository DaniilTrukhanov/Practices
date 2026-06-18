import datetime

x = datetime.datetime.now()
x -= datetime.timedelta(days=1)
print (f"Yesterday is {x}")

x = datetime.datetime.now()
print (f"Today is {x}")

x += datetime.timedelta(days=1)
print (f"Tomorrow is {x}")
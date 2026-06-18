import datetime

x = datetime.datetime.now()
year = int(input("Your year: "))

x = x.replace(year=year)
print (x.strftime("%a"))
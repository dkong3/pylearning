import datetime

help(datetime)

now=datetime.datetime.now()

print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now)
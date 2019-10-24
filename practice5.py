import datetime
import math

# help(datetime.date)
d1=datetime.date(2014, 7, 2)
d2=datetime.date(2014, 7, 11)
delta = d2-d1
print(delta.days)
print("%3.5f" %(math.pi*4/3*6**3))

def diff(n):
    if n>17:
        return 2*(n-17)
    else:
        return 17-n

print(diff(22))
print(diff(3))

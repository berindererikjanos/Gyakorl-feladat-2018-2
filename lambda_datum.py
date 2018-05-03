import datetime
import math

days = lambda y1,m1,d1,y2,m2,d2 : str((datetime.date(y2,m2,d2)-datetime.date(y1,m1,d1)).days)+" days"
print(days(1998,4,17,2018,5,3)

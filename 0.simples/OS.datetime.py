
#DATE TIME module examples

from datetime import datetime
from datetime import date
from datetime import time

#prints year,month,day
today=date.today()
print (today)
print (today.year,"-",today.month)


#prints year,month,day
now1=datetime.now()
print(now1)
print(now1.year,"/",now1.month,"/",now1.day ,"///",now1.hour)
print(now1.strftime("%d-%m-%y-%A"))

if datetime.now() > datetime(2018,7,7):
    print ("echo")

#print time 24 hr format
print(now1.strftime("%H:%M"))
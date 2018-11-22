
#DATE TIME module examples

from datetime import datetime
from datetime import date
from datetime import time

"""""

#prints year,month,day  ## USING DATETIME
#-------------------------------------------------
now1=datetime.now() 
print(now1)
print(now1.year,"/",now1.month,"/",now1.day ,"///",now1.hour)
print(now1.strftime("%d-%m-%y-%A"))

#print time 24 hr format
print(now1.strftime("%H:%M"))


#prints year,month,day  ## USING DATE module
#----------------------------------------------------------
today=date.today()
print (today)
print (today.year,"-",today.month)

"""""
from datetime import datetime
if datetime.now() > datetime(2018,11,22,15,28):
    print( "LATEST TIME :"+datetime.now().strftime("%d-%m-%y  :- %H-%M"))
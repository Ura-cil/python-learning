#time table

import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
# hour=int(input("enter hour"))
print(hour)

if(hour>=0 and hour<12):
   print("good morning ")
elif(hour>=12 and hour<17):
   print("good aternoon")   
else:
   print("good night")   
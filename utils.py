#importing a library to code
import os
import datetime
#add commands depending on the OS
#print(os.system('systeminfo'))

#creating functions for OS commands

def check_systemInfo() :
    print(os.system('systeminfo'))

#def check_date():
   # print(os.system('date'))


check_systemInfo()
#check_date()

today = datetime.date.today()
print(today)

#functions in python
#functions are written using "def" as prefix

import os

def check_date(command) :
    print(os.system(command))      #date command shows date from OS


def addNumbers(num1,num2):       #function to add numbers
    sum=num1+num2
    print("The sum is ",sum)

addNumbers(25,56)
check_date("date")



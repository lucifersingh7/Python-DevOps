#functions in python
#functions are written using "def" as prefix

import os
import datetime

def addNumbers(num1,num2):       #function to add numbers
    sum=num1+num2
    print("The sum is ",sum)

addNumbers(25,56)

def findProduct(x,y) :
    result = x*y
    print ("The product is ",result)

findProduct(122,57)

def check_Date() :
    return datetime.date.today()
today = check_Date()

print(today)








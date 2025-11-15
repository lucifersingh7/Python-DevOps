#functions tutorial for Python programming

#function to find the product of all numbers

list = [12,45,18,7,10,99,17]

def findProduct(list):
    product=1
    for x in list:
        product = product*x
    print("The result is",product)

findProduct(list)

#function to find odd or even 

def OddEven(list) :
    for i in list :
        if (i%2 == 0) :
            print("Even number")
        else :
            print("Odd Number")

OddEven(list)


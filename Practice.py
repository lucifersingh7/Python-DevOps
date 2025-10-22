# Python function to find the maximum of three numbers

first_num=input("Enter first number : ")
second_num = input("Enter second number : ")
third_num = input("Enter third number : ")

def show_max(x,y,z) :
    if x > y and z :
        print( x," is greater")
    elif y > z and x :
        print(y," is greater")
    elif z > x and y :
        print(z," is greater")

show_max(first_num,second_num,third_num)


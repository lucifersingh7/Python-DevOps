#Basic python program Calculator 

firstNum=int(input("Enter first Number : "))
secondNum = int(input("Enter the second Number : "))

operator = input("Choose Operator(+,-,/,*) : ")

if operator == "+" :
    sum = (firstNum+secondNum)
    print("The sum is ", sum)
elif operator == "-" :
    diff = (firstNum - secondNum)
    print("The difference is ", diff)
elif operator == "*" :
    product = (firstNum*secondNum)
    print("The product is", product)
elif operator =="/" :
    result = (firstNum/secondNum)
    print("The resut is",result)
else :
    print("Invalid Operator")
    


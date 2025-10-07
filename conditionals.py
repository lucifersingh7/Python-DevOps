#This is a simple calculator program using conditional operators
num1 = int(input("Enter the First Number : "))
num2 =int(input("Enter the Second Number : "))

choice = input("Enter operator-----> ( + , - , / , *, %)   : ")

if choice == "+" :
   sum = num1 + num2
   print("Sum : ",sum)

elif choice == "-" :
   diff = num1 - num2
   print("Difference : ",diff)

elif choice =="/" :
   quotient = num1/num2
   print ("Quotient : ",quotient)

elif choice == "*" :
   product = num1*num2
   print("Product : ",product)

elif choice == "%" :
   remainder = num1%num2
   print("Remainder : ",remainder)

else :
   print("Invalid Operator selected ")


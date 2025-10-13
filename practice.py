#This is a practice demo tutorial
print('This is a Python tutorial')
print("This is my calculator")

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

choice = input("Enter the operators(+,-,/,*,%) :  ")

if choice == "+" :
    result = first_number + second_number
    print("Sum is ",result)

elif choice == "-" :
    result = first_number - second_number
    print("The difference is",result)

elif choice == "/" :
    result = first_number / second_number
    print("The quotient is ",result)

elif choice == "*" :
    result = first_number * second_number
    print("The product is",result)

elif choice == "%" :
    result = first_number % second_number
    print("The remainder is",result)

else :
    print("The operator you've entered is invalid.")


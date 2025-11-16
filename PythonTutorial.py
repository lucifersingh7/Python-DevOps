#write a function to find whether a given number is prime number or not.

number = int(input("Enter the number to check : "))

def find_Prime_number(num):
     if (num%2==1) :
          print("The number is a prime number")
     elif (num%2==0) :
          print("Number is a composite number")
     else :
          print("Not a prime number")

find_Prime_number(number)

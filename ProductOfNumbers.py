#Write a Python function to multiply all the numbers in a list.

first_num = int(input("Enter number : "))
second_num = int(input("Enter number : "))
third_num = int(input("Enter number : "))
fourth_num = int(input("Enter number : "))
fifth_num = int(input("Enter number : "))
sixth_num = int(input("Enter number : "))
seventh_num = int(input("Enter number : "))

numbers = [first_num,second_num,third_num,fourth_num,fifth_num,sixth_num,seventh_num]   #list or array

def show_product(numbers) :
    result = 1
    for i in numbers :
        result = result * i
    return result

print("The product is", show_product(numbers))

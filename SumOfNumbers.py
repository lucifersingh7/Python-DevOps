# To Find Sum Of Numbers in a List

list = [12,45,17,18,7,10,99,333]

def find_sum(list) :
    sum = 0
    for x in list :
        sum = sum+x
    
    return sum


print("The sum of numbers is ",find_sum(list))

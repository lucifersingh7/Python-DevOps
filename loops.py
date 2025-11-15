#forloop tutorial for Python

list =["azure","aws","salesforce","oracle"]
print(list)
#Using append command
list.append("Heroku")
print(list)
#using Insert command
list.insert(3,"IBM")
print(list)

#printing all the elements in the list
for x in list :
    print(x)


#add all the numbers in the list
myList=[12,17,15,14,55,48,51]
sum=0

for i in myList :
    sum = sum+i
    
print("The sum is",sum)
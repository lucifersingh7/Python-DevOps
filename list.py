#print a list/array

list_clouds = ["aws",25.12,"azure","oracle",18,"bubble"]
array = [20,35,47,25,26,18,45]

print(list_clouds)
print(array)

#print the length of the list
length = len(list_clouds)
print("The length of List :",length)
print("The length of Array :",len(array))

#add data into the list.
list_clouds.append("newData")
print(list_clouds)

#Insert data into list on index 3
list_clouds.insert(3,"New Data")
print(list_clouds)

#Remove data from list and array
list_clouds.remove(25.12)
print(list_clouds)


#create an empty list called my_list
my_list = []

#Appending values to my_list 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("Append:", my_list)


#insert 15 at the second position
my_list.insert(1, 15)

print("insert 15:", my_list)

#extending my_list with new value
my_list.extend([50, 60, 70])
print(my_list)

#Remove the last element in my_list
my_list.pop(7)
print(my_list)

#Sort my_list in ascending order
my_list.sort()
print(my_list)

#Find the index of 30 and print its value
value = 30
num = my_list.index(30)
print("The value index is:", num)


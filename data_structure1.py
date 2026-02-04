# Creating a tuple
my_tuple = (10, 20, 30, 40, 50, 60)
print("Tuple :",my_tuple)

print("First element :",my_tuple[0])
print("Last element :",my_tuple[5])

print("Slice [1:4] :",my_tuple[1:4])
print("Slice from beginning to index 3 :",my_tuple[:3])
print("Slice from index 2 to end :",my_tuple[2:])

extra_tuple =(70,80,90)
concatenated = my_tuple + extra_tuple
print("Concatenated Tuple :",concatenated)

for item in my_tuple:
    print("Item :",item)

print("Is 30 in tuple?",30 in my_tuple)
print("Is 100 not in tuple?",100 not in my_tuple)

nested_tuple =(my_tuple,(70,80,90))
print("Nested Tuple :",nested_tuple)
print("Accessing nested element (my_tuple[2]) :",nested_tuple[0][2])
print("Accessing nested element (90) :",nested_tuple[1][2])

print("Length of Tuple :",len(my_tuple))
print("Maximum value :",max(my_tuple))
print("Minimum value :",min(my_tuple))
print("Sum of elements :",sum(my_tuple))

temp_list = list(my_tuple)
temp_list[2] = 99 # Update 3rd element
updated_tuple = tuple(temp_list)
print("Updated Tuple :", updated_tuple)

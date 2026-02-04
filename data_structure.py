# 1.Creating a List
fruits =["apple","banana","cherry","mango","orange"]
print("Original List :", fruits)

# 2.Accessing Elements in a List
first_fruit = fruits[0]
last_fruit = fruits[-1]
print("First Fruit :",first_fruit)
print("Last Fruit :",last_fruit)

# 3.Slicing a List
sublist_fruits = fruits[:3]
print("Sublist of first three fruits :",sublist_fruits)

# 4.Adding Elements to a List
fruits.append("grape")
print("List after adding 'grape' :", fruits)

# 5.Inserting Elements into a List
fruits.insert(1,"pineapple")
print("List after inserting 'pineapple' at position 1 :",fruits)

# 6.Removing Elements from a List
fruits.remove("banana")
print("List after removing 'banana' :",fruits)

# 7.Poping Elements from a List
popped_fruit = fruits.pop() # Remove and returns the last item
print("Popped fruit :",popped_fruit)
print("List after popping the last element :",fruits)

# 8.Finding the Length of a List
length = len(fruits)
print("Number of fruits in the list :",length)

# 9.Checking Membership in a List
is_in_list = "apple" in fruits
print("Is 'apple' in the list?", is_in_list)

# 10.Iterating Over a List
print("Iterating Over a List :")
for fruit in fruits:
    print(fruit)

# 11.Sorting a List
fruits.sort()
print("List after sorting alphabetically :",fruits)

# 12.Reversing a List
fruits.reverse()
print("List after reversing the order :",fruits)

# 13.List Comprehensions
long_fruits =[fruit for fruit in fruits if len(fruit) > 5]
print("Fruits with more than 5 letters :",long_fruits)

# 14.Coping a List
fruits_copy = fruits.copy()
print("Copied list :",fruits_copy)

# 15.Clearing a List
fruits.clear()
print("List after clearing all elememts :",fruits)

# 16.Extending a List with Another List
vegetables = ["carrot","broccoli","spinach"]
fruits_copy.extend(vegetables)
print("List after extending with vegetables :",fruits_copy)

# 17.Counting Occurrences of an Element in a List
num_apples =fruits_copy.count("apple")
print("Number of 'apple' in the list :",num_apples)

# 18.Finding the Index of an Element
if "carrot" in fruits_copy:
    carrot_index = fruits_copy.index("carrot")
    print("Index of 'carrot' :", carrot_index)

# 19.Removing an Element by Index
if len(fruits_copy)> 2:
    del fruits_copy[2]
print("List after removing elememts at index 2 :",fruits_copy)

# 20.Nested Lists
nested_list = [fruits_copy,vegetables]
print("Nested List :",nested_list)

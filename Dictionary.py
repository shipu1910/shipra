# 1.Creating a Dictionary
student_grades = {
    "Manika" : 85,
    "Sita" : 78,
    "Riya" : 62,
}
print("Student Grade :",student_grades)

# 2.Accessing Dictionary Values
alice_grade = student_grades["Manika"]
print("Manika's Grade :",alice_grade)

# 3.Adding a New Key-Value Pair
student_grades["Roshni"] = 88
print("Updated Student Grade :",student_grades) 

# 4.Removing a Key-Value Pair
student_grades.pop("Sita")
print("Student Grades after removing Sita :",student_grades)

# 5.Checking Key Membership
is_Roshni_in_dict = "Roshni" in student_grades
print("Is Roshni in the dictionary?",is_Roshni_in_dict)

# 6.Iterating Over a Dictionary (Keys and Values)
print("Iterating Over student names and grades :")
for student, grade in student_grades.items():
    print(f"{student} : {grade}")

# 7.Using the get() Method 
Riya_grade = student_grades.get("Riya","Not found")
print("Riya's Grade :",Riya_grade)

# 8.Merging Dictionaries
additional_grades = {"Bhawani": 60, "Usha": 75}
student_grades.update(additional_grades)
print("Student Grades after merging with additional data :",student_grades)

# 9.Dictionary Comprehension
squared_numbers = {x: x** 2 for x in range(1, 6)}
print("Dictionary of numbers and their squares :",squared_numbers)

# 10.Handling Nested Dictionaries
nested_dick = {
    "USA" :{"New York" : 8000000, "Los Angeles" : 4000000},
    "India" :{"Mumbai" : 20000000, "Delhi" : 15000000}
}
print("Nested Dictionaries of countries and cities :",nested_dick)

# Accessing nested values
ny_population = nested_dick["USA"] ["New York"]
print("Population of New York :",ny_population)

# 11.Clearing and Copying Dictionaries
student_grades_copy = student_grades.copy()
print("Copy of student grades :", student_grades_copy)

student_grades.copy()
print("Student grades after clearing :", student_grades)
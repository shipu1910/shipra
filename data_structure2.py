# 1.Creating and Accessing Strings
my_string = "Hello, Anamika!"
print("Original string :", my_string)
print("First character :", my_string[0])
print("Last character :", my_string[-1])

# 2.String Concatenation and Repetition
str1 = "Edunet"
str2 = "Foundation"
concat_str = str1 +" " + str2 # Concatenation
repeated_str = concat_str*3   # Repetition
print("Concatenated string :",concat_str)
print("Repeated string :",repeated_str)

# 3.String Case Manipulation
upper_str = my_string.upper()
lower_str = my_string.lower()
title_str = my_string.title()
swapcase_str = my_string.swapcase()
print("Uppercase :",upper_str)
print("Lowercase :",lower_str)
print("Titlecase :",title_str)
print("Swapcase :",swapcase_str)

# 4.Searching in Strings 
substring = "Anamika"
found_index = my_string.find(substring)
if found_index != -1:
    print(f"Substring '{substring}' found at index {found_index}")
else:
    print(f"Substring '{substring}' not found") 

# 5.Replacing Substrings
new_string = my_string.replace("Anamika","World")
print("String after replacement :",new_string)

# 6.String Formatting 
name= 'Anu'
age= 18
formatted_str = f"My name is {name} and I am {age} year old."
print("Formatted string :",formatted_str)

# 7.Implementation of Trimming and Padding String
# Original string with extra spaces
text = "    extra spaces    "
# Padding example (manually adding * characters)
padded = "*** Hello, Edunet!***"
print("Padded string :",padded)
# Trimming example (removing leading and trailing spaces)
trimmed = text.strip()
print("Trimmed string :",trimmed)

# 8.Splitting and Joining Strings
sentence = "Python is fun"
words = sentence.split()  # Splitting based on space
joined_sentence = '-'.join(words)  # Joining with hyphen
print("Splitted words :",words)
print("joined sentence :",joined_sentence)

# 9.Counting Characters 
char_count = my_string.count("o")
print(f"Character 'o' appears {char_count} times in the string")

# 10.Checking String Properties
is_alpha = "Hello".isalpha()
is_digit = "12345".isdigit()
is_alnum = "Hello123".isalnum()
is_space = "   ".isspace()
print("Is 'Hello' alphabetic?",is_alpha)
print("Is '12345' numeric?",is_digit)
print("Is 'Hello123' alphanumeric?",is_alnum)
print("Is '    ' all spaces?",is_space)

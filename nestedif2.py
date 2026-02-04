# Login System
username = input("Enter Username :")
password = input("Enter Password :")
if username == "admin":
    if password == '1234':
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invalid username")            

# # Temperature check
# temp = int(input("Enter Temperature (C) :"))
# if temp > 0:
#     if temp < 20:
#         print("It's cool.")
#     else: 
#         print("It's worm.")
# else:
#     print("It's freezing!")

# # Movie Ticket Discount
# age = int(input("Enter age :"))
# day = input("Enter day(Monday to Sunday) :")
# if age < 12:
#     if day == "Sunday":
#         print("Free ticket for kids!")
#     else:
#         print("Half price ticket")
# else:
#     print("Full price ticket.")

# # Even divisible by 5
# num = int(input("Ask user for a number :"))
# if num % 2 == 0:
#     if num % 5 == 0:
#         print("Even and Divisible by 5")
#     else:
#         print("Even but not Divisible by 5")
# else:
#     print("Odd number")                           
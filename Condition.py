# # if, elif, else conditional statement
mark = int(input("Enter your marks :"))
if mark >= 90:
    print("A")
elif mark >= 75:
    print("B")
elif mark >= 50:
    print("C")
else:
    print("Fail")

# # balance = 100
# # withdraw = int(input("Enter amount to withdraw :"))
# # if withdraw <= balance:
# #     print("Transaction Succefully!")
# # else:
# #     print("don't have balance!")  


# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")  

temp = int(input("Enter your Temperature :"))
if temp > 30:
  print("It is hot day!")
elif temp > 20:
  print("It is nice,worm day!")
elif temp > 10:
  print("It's bit chilly day!")
else:
  print("It's cold outside!")  

# # vehical_type = "two wheeler"
# # vehical_name = "four wheeler"
# # vehical = input("Enter vehical :")
# # if vehical_type == "TVS":
# #   print("This is a bike.")
# # elif vehical_name == "Toyota": 
# #   print("This is four wheeler.") 
# # else:
# #   print("unknown vehical!" )

# vehical = input("Enter your vehical :")
# if vehical in ["XUV","sedan","Nano","Nexon","Bike"]:
#   print("It is a four wheeler vehical.")
# elif vehical in("Bullet","Apache","Splendor","Scooty"):
#   print("It is two wheeler vehical.")
# else:
#   print("Unknown vehical!")   

weather = "Rainy"
if weather == "Rainy":
   print("Go with umbrella")
elif weather == "Sunny":
   print("Go on walk")
else:
   print("Stay at home")        
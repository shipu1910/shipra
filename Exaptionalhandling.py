# try:
#     a = 5
#     b = int(input("enter number :"))
#     print(a/b)
# except ZeroDivisionError:
#     print("not define")

# try:
#     x = 7
#     y = int(input("Enter a number :"))
#     print(x*y)
# except:
#     print("number not define") 

# try:
#     # p = 8
#     q = int(input("Enter a number :"))
#     print(10/q)
# except ZeroDivisionError:
#     print("con't define zero")    
# except ValueError:
#     print("code define define by step") 
# else:
#     print("input the number :",q)
# finally:
#     print("All code done")    

# a = "4"
# d = 6
# print(a+d)

# try:
#     trade = "CSA"
#     print(trede)
# except NameError:
#     print("print error") 

# x = "Anu"
# print(x.upper)
# print(x.cvd)       

# d = ["a","d","c","g"]
# print[5]

# User define error handling
# class nstiadmission(Exception):
#     pass
# try:
#     x = int(input("Enter qualification :"))
#     if x<12:
#         raise nstiadmission("You are not eligible for admission")
#     else:
#         print("You are eligible for admission")
# except nstiadmission as anu:
#     print("Reason :",anu)

# class aadarcord(Exception):
#      pass
# try:
#      x = input("Enter valid aadar number :")
#      if len(x) != 12:
#           raise aadarcord("Enter a valid 12 digit number")
#      else:
#           print("Aard number accpeted")
# except aadarcord as kali:
#      print("Reason :",kali)          

# 1. Predict the output:
try:
       print("Before error")
       print(5 / 0)
except:
       print("Something went wrong")



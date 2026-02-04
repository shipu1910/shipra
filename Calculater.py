# file Handling
# text = input("Write something :")
# file = open("abc.txt","w")
# file.write(text)
# file.close()
# file = open("abc.txt","r")
# content = file.read()
# print("File Content :",content)
# file.close()

# Login System
# username = "admin"
# password = "24072006"
# u = input("Enter Username :")
# p = input("Enter Password :")
# if u == username and p == password:
#     print("Login Successful!")
# else:
#     print("Login Failed!")

# Simple Calculater 
num1 = float(input("Enter First Number :"))
num2 = float(input("Enter Second Number :"))
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Choose an option :"))
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
elif choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1/num2)
else:
    print("Invalid Choice")            


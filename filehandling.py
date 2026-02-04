# x = open("abc.txt","r")
# y = x.read()
# print(y)

# x = open("abc.txt","w")
# x.write("This is new contant\n")
# x.write("Welcome to new code\n")

# x = open("abc.txt","a")

# x.write("""This is new contant
# Welcome to new code
# new contant added\n""")
# file = open("abc.txt","r")
# file.close


# with open("abc.txt","r")as file:
#     print(file.read())


# with open("abc.txt","a")as file:
#     file.write("We are Indians\n")
#     file.write("We live in india\n")
# print("Data appended successfully!")   

# with open("abc.txt","r")as file:
#     lines= file.readlines()
#     word = "Welcome to new code"
#     with open("abc.txt","w")as file:
#         for line in lines:
#             if word not in line:
#                 file.write(line)    

remove = 1
with open("abc.txt","r")as f:
    lines = f.readlines()
    with open ("abc.txt","w")as f:
        for i, live in enumerate (lines):
            if i != remove:
                f.write(live)










# Local variable
def local():
    name = "Adit"
    print(name)
local()

# Two functions with their own local scope
def fun1():
    a = 20
    print("fun1 variable :",a)
def fun2():
    b = 40
    print("Fun2 variable :",b)
fun1()
fun2()

# Global variable
course = "Python"
def show_course():
    print("Enrolled in :",course)
show_course()
print("Outside Function :",course) 

# Same Global variable
institute = "NSTI Allhabad"
def welcome():
    print("Welcome to :",institute)
def info():
    print("Institute name is :",institute)
welcome()
info()

# Global Keyword
count = 0
def increase():
    global count
    count += 1
    print("Count is now :",count)
increase()
increase()
increase()
increase()
increase()

# 1.Global Variable
college = "NSTI W"
def xyz():
    print(college)
xyz()
print(college)

# 2.Local Variable
def local():
    college = "NSTI W"
    print(college)
local()

# Global + Local variable
college = "NSTI W"
def globals():
    college = "Allhabad"
    print(college)
globals()
print(college)

name = "Anuradha"
def info():
    adderes = "Kanpur"
    print(adderes)
info()
print(name)    

# 3.Global Keyword
name = "Radha"
def mk():
    global name
    name = "Anshu"
    print(name)
mk()
print(name)


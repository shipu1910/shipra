# Adding in function
def add(a,b):
    return a+b
print(add(55,98))

# Substract in function
def sub(x,y):
    z=x-y
    return z
# sub()
print(sub(67,56))

# Multiplcation in function
def multi(p,q):
    return p*q
print(multi(34,25))

# Division in function
def div(a,b):
    if b!=0:
        return a/b
    else:
        return "Invalid"
print(div(10,0))   

# Squre in function
def squr(a):
    return a**2
print(squr(22))

# Factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num =int(input("Enter Number :"))
print("Factorial of",num,"is :",factorial(num))
    

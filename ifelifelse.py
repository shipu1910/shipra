# Temperature Checker
temp = int(input("Enter your Temperature :"))
if temp > 30:
  print("It's hot day!")
elif 20<= temp <= 30:
  print("Nice weather!")
else:
  print("It's cold today!")  

# Student Grading System
mark = int(input("Enter your marks :"))
if mark >= 90:
    print("Grade A")
elif mark >= 75:
    print("Grade B")
elif mark >= 50:
    print("Grade C")
else:
    print("Fail")

# Traffic Signal Decision
color = input("Enter the signal color (red, yellow, or green): ")
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid color")  

# Even or Odd Number
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("Even number")
else:
    print("Odd number")

# Movie Ticket Discount
age = int(input("Enter your age: "))
if age < 12:
    print("Ticket price: 100")
elif 12 <= age <= 60:
    print("Ticket price: 200")
elif 60 <= age <=85:
    print("Ticket price: 150")
elif age > 85:
    print("Ticket price: 300")    
else:
    print("Invalid age")  
    
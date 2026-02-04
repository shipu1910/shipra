# Voting Eligibility
age =int(input("Enter your age :"))
if age >= 18:
    citizen = input("Enter your citizenship :")
    if citizen == "Indian":
        print("Eligible to vote in India.")
    else:
        print("No eligible due to citizenship.")
else:
    print("Not eligible due to age.") 

# Student Grade
marks = int(input("Enter your marks :"))
if marks >= 40:
    if marks >= 90:
        print("Excellent")
    elif marks >= 75:
        print("Very Good")
    else:
        print("Good")
else:
    print("Fail")  

# Online Shopping Discount
purchase_amount = int(input("Enter your purchase amount :"))
if purchase_amount >1000:
    is_member = input("Are you a member? (Yes/No) :")    
    if is_member == 'yes':
        print("20% discount applied")
    else:
        print("10% dicount applied")
else:
    print("No discount available.")

# Exam Result Checker
marks = int(input("Enter marks (in %): "))
if marks>= 40:
    attendance = int(input("Enter attendance (in%): "))
    if attendance>= 75:
        print("Pass")
    else:
        ("Pass but low attendance worning")
else:
    print("Fail")            


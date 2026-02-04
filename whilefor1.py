# num = 2
# while num <=4:
#     print("\nTable of :",num)
#     for i in range(1,11):
#         print(num,"X",i,"=",num*i)
#     num += 1  

# round_num = 1
# while round_num <= 3:
#     print("Round :",round_num, end= " ")
#     for i in range(round_num):
#         print("*", end=" ")
#     print()
#     round_num += 1  

# day = 1
# while day <= 3:
#     print("Day :",day,end=" ")
#     for time in ("Morning","Afternoon","Evening"):
#         print(time,end=" ")
#     print()
#     day += 1            

# user = 1
# OriginalBalance ={1:1000,2:5000,3:7000}
# while user <= 3:
#     print("User :", user)
#     balance = OriginalBalance[user]
#     for i in range(1,4):
#         amount =int(input("Enter your amount :"))
#         if amount <=balance:
#             balance +=amount
#         print("Remaining Balance :", balance)
#     # else:
#     #     print("Insufficient Balance")
#     print("User :",user,"Transanction Completed")
#     user += 1  



# customer =1
# while customer<=2:
#     print("Customer :",customer)
#     total = 0
#     for i in range(1,3):
#         amount=int(input("Enter your amount :"))
#         total =total+amount
#     print("Total Bill :",total)
#     print("Next Customer")
#     customer +=1  

# customer =1
# while customer<=2:
#     print("Customer :",customer)
#     LoanAmount =int(input("Enter your Loan Amount :"))
#     rate = int(input("Enter your rate :"))
#     year =int(input("Enter your year :"))
#     for i in range(year):
#         amount=LoanAmount*(rate/100)
#         LoanAmount=LoanAmount+amount
#     print("LoanAmount :",LoanAmount)
#     print("Next Customer")
#     customer +=1  

Student =1
while Student <=3:
    print("Student :", Student)
    total =0
    for subject in range(1,6):
        marks =int(input("Enter marks for subject :"))
        total =total + marks
    average =total/5
    print("Total Marks :",total)
    print("Average Marks :",average)
    print("Next Student!")
    Student +=1    


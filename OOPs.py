# class student:
#     def __init__(self,name,trade):
#         self.name = name
#         self.trade = trade
# stu1 = student("Arpita","DM")
# stu2 = student("Radha","COPA")
# print(stu1.name,stu1.trade) 
# print(stu2.name,stu2.trade)   

# class ticket:
#     def __init__(self,moviename, ticketprice):
#         self.moviename = moviename
#         self.ticketprice = ticketprice
# mov1 = ticket("Fir Hera Feri", "190")
# mov2 = ticket("Dangal", "200")
# mov3 = ticket("Bhootnath", "150")
# print(mov1.moviename,mov1.ticketprice)
# print(mov2.moviename,mov2.ticketprice)
# print(mov3.moviename,mov3.ticketprice)

# # Bank Account
# class BankAccount:
#     def __init__(self,balance):
#         self.balance =balance
#     def add(self,amount):
#         self.balance +=amount
#     def withdraw(self, amount):
#         self.balance -= amount
#     def finalAmount(self):
#         return self.balance
# acci = BankAccount(500)
# acci.add(1000)
# acci.withdraw(600)
# print(acci.finalAmount())       
                
# Bank Account input user
class BankAccount:
    def __init__(self,balance):
        self.balance =balance
    def add(self,amount):
        self.balance +=amount
    def withdraw(self, amount):
        self.balance -= amount
    def finalAmount(self):
        return self.balance
initial = int(input("Enter your amount :"))
deposit = int(input("Enter your depositamount :"))
credit = int(input("Enter your creditamount :"))      
acci = BankAccount(initial)
acci.add(deposit)
acci.withdraw(credit)
print(acci.finalAmount())


class account:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    # def add_amount(self,amount):
    #     self.__balance += amount
    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def show_balance(self):
        return self.__balance
A1 = account("ABC Bank",2000)
# A1.add_amount(500)
A1.withdraw(600)
print(A1.show_balance())

# class ATM:
#     def __init__(self,pin,balance):
#         self.__pin = pin
#         self.__balance = balance
#     def check_balance(self,pin):
#         if pin == self.__pin:
#             return self.__balance
#         else:
#             return "Incorrect Pin"
# x = ATM(6633,2233)
# print(x.check_balance(6633))

class Employee:
    def __init__(self):
        self.name = ""
        self.__salary = 0

    def set_details(self,name,salary):
        self.name = name
        if salary > 0:
            self.__salary = salary
      
    def showname(self):
        print(self.name)

    def update_salary(self,amount):
        if amount > 0:
            self.__salary = self.__salary + amount
        else:
            print("Positive Amount")

    def show_salary(self):
        print("salary",self.__salary)

emp = Employee()
emp.set_details("Arpita",3500)
emp.showname()
emp.update_salary(500)
emp.show_salary()    
            
                                

# class Student:
#     def __init__(self,name,phoneno,adharno):
#         self.name = name
#         self._phoneno = phoneno
#         self.__adharno = adharno
#     def classregister(self):
#         print(self.__adharno)
# R1 = Student("Anupama",9135678923,345678962345)
# print(R1.name,R1._phoneno, R1._Student__adharno)

# class Account:
#     def __init__(self,name,balance):
#         self.name = name
#         self.__balance = balance
#     def deposit_amount(self,amount):
#         self.__balance += amount
#     def withdraw_amount(self,amount):
#         if amount <= self.__balance:
#             self.__balance -= amount

#     def get_balance(self):
#         return self.__balance
# A1 = Account("ABC Bank",2000)
# A1.deposit_amount(500)
# A1.withdraw_amount(600)
# print(A1.get_balance())

# class Student:
#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number
#     def display_details(self):
#         print("Student Name:" ,self.name)
#         print("Roll Number:", self.roll_number)
# student1 = Student("Akriti", 11)
# student2 = Student("Priya", 12)
# student1.display_details()
# student2.display_details()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def person_details(self):
#         print("Name:" , self.name)
#         print("Age:" ,self.age)
# user_name = input("Enter your name: ")
# user_age = input("Enter your age: ")
# x = Person(user_name,user_age)
# print(x.name,x.age)

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def circumference(self):
        return 2 * math.pi * self.radius
if __name__ == "__main__":
    c = Circle(2)
    print(c.area())
    print(c.circumference())    
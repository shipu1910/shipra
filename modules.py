# # def add(a,b):
# #     return a+b
# # def hello():
# #     print("Welcome to NSTIW")

# import math
# print(math.sqrt(9))
# print(math.pow(3,4))
# print(math.pi)
# print(math.factorial(5))

import datetime
now = datetime.datetime.now()
today = datetime.date.today()
future = today +datetime.timedelta(days=10)
print("10 days later :",future)
print(today)
print(now)
print(now.year)
print(now.month)
print(now.day)

# import sys
# print(sys.version)
# print(sys.executable)
# print(sys.platform)

# import random
# print(random.randint(1,10))
# print(random.random())
# print(random.choice(["AIPA","CSA","COPA","EM","DM"]))
# trade = ["AIPA","COPA","EM","DM"]
# random.shuffle(trade)
# print(trade)

# import os
# print(os.getcwd())
# print(os.listdir())
# # os.mkdir("AI")
# os.rmdir("AI")

import time
print(time.ctime())
time.sleep(5)
print("After 5 second")



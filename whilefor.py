number = 0
Trade = ["CSA","AIPA","COPA","EM"]
while number < len(Trade):
    print("\nTrade name :",Trade[number])
    print("Student Roll Numbers :")
    for i in range(1,6):
        print("Roll No :", i )
    print("Trade wise attendance done!")
    number +=1  

import time
classname = 0
while classname <=5:
    print("Class :", classname)
    for i in range(1,11):
        print(i,end = " ")
        time.sleep(0)
    print("\n Attendance Done")
    classname += 1



import time
for round in range(1,4):
    print("Round :", round)
    count = 3
    while count >0:
        print("Countdown :",count)
        time.sleep(2)
        count -=1
    print("Round Completed!")  
    print("Next Round!")                  


import time
round = 1
while round <=5:
    print("Countdown :",round)
    for i in range(1,6):
        print(i,end =" ")
        time.sleep(2)
    print("Round Completed!")  
    print("Next Round!")
    round += 1

# for num in range(2, 20):
#     is_prime = True
# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break
#     if is_prime:
#         print(f"{num} is a prime number")
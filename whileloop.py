num = int(input("Enter a number :"))
while num>0:
    print(num)
    num -= 1
print("Loop end here")  

money =0

while money <4000:
    money += 50
    print("Added money :",money)
print("Money collected!")    

import time
num = 5
while num>0:
    print(num)
    num -= 1
    time.sleep(2)
print("Time's Up")  

import time
classname = 0
while classname <=5:
    print("Class :", classname)
    for i in range(1,11):
        print(i,end = " ")
        time.sleep(0)
    print("\n Attendance Done")
    classname += 1 

classname = 1
while classname <=8:
    print("\n Class :", classname)
    print("Roll no  Name  Marks")
    for i in range(1,7):
        name = "Student" + str(i)
        mark = (i*10) + 30
        print(i, "  ",name, "  ",mark, "  ")
    print("Mark Done!")
    classname += 1  





# def list(*args):
#     print("First of students :")
#     for i in args:
#         print(i)
# list("AIPA","CSA","EM","COPA")

# def add(*args):
#     print("Add numbers :")
#     sum = 0
#     for i in args:
#         sum +=i
#     return sum
# print(add(1,2,3,4,5,6))

# def abc(*args):
#     print("Sum of numbers :")
#     sum =0 
#     for i in args:
#         sum+=i
#     return sum
# # print(abc(1,2,3,4,5)) 
# xgs =input("Enter your marks :")
# fgh =[int(x) for x in xgs.split()]
# print(abc(*fgh))   

# 2.Take space-separated numbers, pass using *args, and print average
# def ave(*args): 
#     print("Average of numbers :")
#     total = 0
#     for i in args:
#         total += i
#     average = total / len(args)
#     return average
# num = input("Enter your number :")
# ave_list =[int(x) for x in num.split()]
# print(ave(*ave_list))  

# 1.Function to find the largest number using
def find_largest(*args):
    return max(args)
print(find_largest(33,45,56,67,89))




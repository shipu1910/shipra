# # 1.Reverse each word without changing order
# sentence = "Python programming is fun"
# words = sentence.split()
# result = " ".join(word[::-1] for word in words)
# print(result)

# # 2.Swap first and last words
# sentence = "Python makes coding easy"
# words = sentence.split()
# words[0],words[-1] = words[-1], words[0]
# result = " ".join(words)
# print(result)

# # 3.Check sentence palindrome(ignore space + case)
# sentence = "Nurses run"
# clean = sentence.replace(" ","").lower()
# if clean == clean[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not a Palindrome")

# # 4.Find longest word(without split())




class MyClass:
       def __init__(self):
            self.num = 1
       def increment(self):
            self.num += 1
obj = MyClass()
obj.increment()
obj.increment()
print(obj.num)
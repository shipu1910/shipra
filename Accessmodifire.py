# Public Access
# class AIPA:
#     def __init__(self,name):
#         self.name = name
#     def display (self):
#         print(self.name)
# N1 = AIPA("Sakshi")
# N1.display()
# print(N1.name)            

# Private Access
# class AIPA:
#     def __init__(self,tools, name):
#         self._name = name
#         self._tools = tools
#     def uses(self):
#         print(self._tools)
# T1 = AIPA("Anu","Almirah")
# T1.uses()
# print(T1._tools, T1._name)    

# Protected Access
class AIPA:
    def __init__(self,name,tools,register):
        self.name = name
        self._tools = tools
        self.__register = register
    def classregister(self):
        print(self.__register)
R1 = AIPA("Anu","Almirah","CR")
print(R1.name,R1._tools, R1._AIPA__register)

# class ACCI:
#     def __init__(self,ceoname,companyname,productname):
#         self.ceoname = ceoname
#         self._companyname = companyname
#         self.__productname =productname
#     def companywork(self):
#         print(self.__productname)
# C1 = ACCI("Rohit Shrama","HP","Computer Parts")
# print(C1.ceoname,C1._companyname,C1._ACCI__productname)           

# Student Record
class StudentRecord:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self._roll_no = roll_no
        self.__marks = marks
    def display_public(self):
        print(self.name)
    def display_protected(self):
        print(self._roll_no)
    def display_private(self):
        print(self.__marks)
S1 = StudentRecord("Akriti",1,79)
S1.display_public()
S1.display_protected()
S1.display_private()            
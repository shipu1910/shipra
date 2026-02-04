# Keyword arguments
# def student_info(**kwargs):
#     print("Student Details :")
#     for key, value in kwargs.items():
#         print(key,":",value)
# student_info(name="Arpita", age =22, course = "Java",city = "Lucknow",Phoneno= 9145673689)

# Positional arguments
# def mix(NSTI,opening = 1992,*trade,**details):
#     print(NSTI)
#     print(opening)
#     if trade:
#         print("Trade in NSTI :",trade)
#     if details:
#         for key,value in details.items():
#             print(key,value)
# mix("Allhabad",2000,"AIPA","CSA","EM","COPA",Phone=9567567894,Pin=211002,email="anu121@gmail.com")            

# 1.Write a function student report
def student_report(name,*subjects,**marks):
    print("Student Name :",name)
    if subjects:
        print("Subjects :",subjects)
    if marks:
        print("   Marks   ")
        for key,value in marks.items():
            print(key,":",value)
student_report("Anamika","Math","Science","English","Hindi","Computer",Math=85,Science=84,English=90,Hindi=94,Computer=90)

# 1.Create a function travel booking
def travel_booking(destination,days=1,*activities,**details):
    print("Destination :",destination)
    print("Days :",days)
    if activities:
        print("Activities :",activities)
        if details:
            print("   Details    ")
            for key,value in details.items():
                print(key,":",value)
travel_booking("Goa",5,"Beach Walk","Scuba Diving","Sunset Cruise",hotal="Sea View Resort",price=25000,transport="Flight")
                
            
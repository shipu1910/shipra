import os
os.mkdir("shipra")

# Rename dirctory
os.rename("shipra","AI")

# Remove dirctory
os.rmdir("AI")

# Rename all files
import shutil

shutil.rmtree ("AI")

# List all files in folder
import os
xyz = os.listdir(".")
print(xyz)

# find out  
PYTHON = os.listdir()
print(PYTHON) (".")

# fide out location of folder
abc = os.getcwd()
print(abc)


import os
os.mkdir("CSA")
with open ("CSA/Student.txt","w")as file:
    file.write("""Student Detail :
               Anamika
               Aakriti
               Sipra
               Priya""")
    print("Ditail add")


import os
os.mkdir("StudentData")
assigments_path = "StudentData/Assignments"
os.mkdir(assigments_path)

os.rename("StudentData","StudentData1")







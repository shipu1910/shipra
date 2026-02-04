# Transport statment
for i in range(1,11):
    if i==3:
        continue
    if i==5:
        continue
    if i==7:
        continue
    print(i)


for i in range(1,11):
    if i==5:
        break
    print(i)


for i in range(1,10):
    pass # placeholder for code
print(i)

for i in range(1,10):
    pass
    for i in range(1,10):
        print(i)
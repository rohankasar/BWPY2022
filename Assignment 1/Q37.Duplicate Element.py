#Q37. Python | Program to print duplicates from a list of integers

Data1 = [1,2,3,3,2,1,5,4,6,8]
print("Original Element : ",Data1)
Data2 = []
for x in Data1:
    if Data1.count(x)>1:
        Data2.append(x)

print("Duplicate Element : ", Data2)

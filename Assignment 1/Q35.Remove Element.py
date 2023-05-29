#Q35. Remove multiple elements from a list in Python

Data1 = eval(input("Enter Original List : "))
Data2 = eval(input("Enter element which you want to remove : "))
print("Original List : " , Data1)
print("Remove element  List : " , Data2)
for i in Data2:
    Data1.remove(i)

print("Final List : " , Data1)
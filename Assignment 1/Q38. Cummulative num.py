#Q38. Python program to find Cumulative sum of a list Break a list into chunks of  size N in

Data1 = [1,2,3,4,5,6,7]
print("Original Hive Table : " , Data1)
Data2 = []
Data3 = 0
for x in Data1:
    Data3 += x
    Data2.append(Data3)
print("Updated Hive Table : " , Data2)
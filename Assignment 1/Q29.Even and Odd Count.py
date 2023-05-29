#Q29. Python program to count Even and Odd numbers in a List

data1 = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1]
data2 = []
data3 = []
data4 = 0
data5 = 0
for x in data1:
    if x%2 == 0:
        data2.append(x)
        data4 = data4 + 1
    else:
        data3.append(x)
        data5 =1 + data5
print("Even Number : ",data2 )
print("Event Count : ", data4)
print("Odd Numbers : ",data3)
print("Odd Count : ", data5)
#Q30. Python program to print positive numbers in a list

data1 = [-1,2,-3,4,-5,6,-7,8,-9]
data2 = []
data3 = 0
for x in data1:
    if x > 0:
        data2.append(x)
        data3 += 1
print("Positive Number : ",data2)
print("Positive Number Count : ",data3)
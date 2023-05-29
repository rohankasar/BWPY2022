#Q34. Python program to count positive and negative numbers in a List

data1 = [1,2,3,4,5,6,7,8,9,-9,-8,-7,-6,-5,-4,-3,-2,-1,-99]
data2 = []
data3 = []
data4 = 0
data5 = 0
for x in data1:
    if x >  0:
        data2.append(x)
        data4 = data4 + 1
    else:
        data3.append(x)
        data5 =1 + data5
print("Positive Number : ",data2 )
print("Positive Count : ", data4)
print("Positive Count Using Length Fun: ",len(data2))

print("Negative Numbers : ",data3)
print("Negative Count : ", data5)
print("Negative Count Using Length Fun: ",len(data3))
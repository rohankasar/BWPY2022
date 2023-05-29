#Q26. Python program to print odd numbers in a list

data1 = [1,2,3,4,5,6,7,8,9]
data2 = [ ]
for x in data1:
    if x%2 != 0:
        data2.append(x)
print(data2)
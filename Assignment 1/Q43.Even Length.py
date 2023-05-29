#Q43. Python program to print even length words in a string

data0 =input("Enter Hive Table to print even words : ")
data1 = data0.split(' ')
data4=''
print(data1)
print(type(data1))
for x in data1:
    data3 = str(x)
    if len(data3)%2 == 0:
        print(data3,end = " ")

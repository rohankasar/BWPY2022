#Q49. Python program to split and join a string

# Data0 = input("Enter String Hive Table : ")
# print("Original String : ", Data0)
#
# Data1 = Data0.split('')
# print('Split String : ',Data1)
#
# Data2 = "-".join(Data1)
# print("Split string after join : ",Data2)



#-----------------------------------

# Data0 = list(input("Enter String Hive Table : "))
# print("Original String : ", Data0)
#
# Data2 = "-".join(Data0)
# print("Split string after join : ",Data2)

#-----------------------------------

Data0 = input("Enter String Hive Table : ")
print("Original String : ", Data0)
data1 = []
x= 1
for i in Data0:
    x += 1
    if  x % 2 != 0 :
        data1.append("-")
    data1.append(i)
    x = 0

print(data1)
Data2 = "".join(data1)
print("Split string after join : ",Data2)




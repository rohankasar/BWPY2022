#Q47. Python | Program to check if a string contains any special character
# Generating random strings until a given string is generated
# Find words which are greater than given length k


# Program to check if a string contains any special character
# Hive Table = 0
# while Hive Table == 0:
#     Data0 = input("Enter string : ")
#     Data1 = input("Enter special charactor : ")
#     Data2 = 0
#     for x in Data1:
#         if x in Data0:
#             Data2 =1
#     if Data2 == 1:
#         print("Special Char Exist ")
#     else:
#         print("Special Char Not Exist !!!!! \n")
#     while True:
#         Data3 = input("Do you want to check next string [y/n] : ")
#         if Data3 == 'y':
#             Data2 = 0
#             break
#         elif Data3 == 'n':
#             Hive Table = 1
#             break
#         elif Data3 != 'y' or 'n':
#             print("Enter Valid data ! ")



# Find words which are greater than given length k
Data0 = input("Enter string : ")
Data1 = int(input("Enter length : "))
Data2 = Data0.split(' ')
Data3 = 0
Data4 = len(Data2)

while Data3 < Data4:
    if len(Data2[Data3])>Data1:
        print(Data2[Data3],end = " ")
        Data3 +=1
    else:
        Data3 += 1




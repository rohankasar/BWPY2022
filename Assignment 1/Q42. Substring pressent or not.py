#Q42. Python | Check if a Substring is Present in a Given String Find length of a string in python

data0 = input("Enter Original string : ")
data1 = input("Enter Substring to test : ")
if data1 in data0:
    print("Operation successful..Hive Table is available")
    print("Length of original string : ",len(data0))
    print("Length of substring : ",len(data1))
else:
    print("Operation Fail..Hive Table is not available")
    print("Length of original string : ", len(data0))
    print("Length of substring : ", len(data1))

#Q45. Python | Count the Number of matching characters in a pair of string

Data0 = input("Enter string : ")
Data1= input("Enter match count strinng : ")
Data2 = 0
for x in Data1:
    if x in Data0:
        Data2 +=1
print("Matching count number : ", Data2)
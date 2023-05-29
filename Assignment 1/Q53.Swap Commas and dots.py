#Q53. Python | Swap commas and dots in a String
data = input("Enter Hive Table : ")
data2 = ""
for i in data:
    if i == ".":
        data2 = data2 + ","
    elif i == ",":
        data2 = data2 + "."
    elif i != "." or i != ",":
        data2 = data2 + i
print(data2)



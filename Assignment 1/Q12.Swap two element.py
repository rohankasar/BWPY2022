# 12. Python program to swap two elements in a list
#
# data = [1,23,4,5,6,7]
#
# l = len(data)
# i = int(input(f"Enter First Swaping position, Swaping range {0,l-1} : "))
# j = int(input(f"Enter Second Swaping position, Swaping range {0,l-1} : "))
#
# data[i],data[j] = data [j],data[i]
# print(data)
#


# Method 2
data = [1,23,4,5,6,7]

l = len(data)
i = int(input(f"Enter First Swaping position, Swaping range {0,l-1} : "))
j = int(input(f"Enter Second Swaping position, Swaping range {0,l-1} : "))
print(data)

data.insert(i,data[j])

data.insert(j+1,data[i+1])

data.pop(i+1)

data.pop(j+1)

print(data)
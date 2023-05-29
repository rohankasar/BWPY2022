# Q.56 Python String slicing in Python to rotate a string

data = "123456789"
data2 = ""
lt = len(data)+1

# with for loop + slicing
for i in range(len(data)+1):
    if i > 0:
        print(data[-i],end="")
print()

# Without Slicing
for i in data:
    data2 = i + data2
print(data2)
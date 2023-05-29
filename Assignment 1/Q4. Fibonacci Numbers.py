# Q4. Python Program for Fibonacci numbers

User_Input = int(input('Enter Number : '))
Temp = [0, 1]

for i in range(User_Input - 2):
    b = Temp[i] + Temp[i + 1]
    Temp.append(b)
print(Temp)

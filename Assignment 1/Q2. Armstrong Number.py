# Q2. Python Program to check Armstrong Number Code:

User_Input  = int(input("Enter number : "))
count = str(User_Input)
lenght = len(count)
Temp = 0

for i in range(lenght):
    b = int(count[i]) ** lenght
    Temp = Temp + b

if Temp == User_Input:
    print('Entered number is Armstrong number ***')
else:
    print('Entered number is not Armstrong number')

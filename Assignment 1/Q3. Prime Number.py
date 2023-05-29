# Q3. Python program to print all Prime numbers in an Interval

print('The starting value must be greater than 1 and less than last value')
Start = int(input('Enter starting number: '))
End = int(input('Enter last number: '))
Temp = []

if Start < End and Start > 1:
    for i in range(Start, End):
        if i != 2:
            for j in range(2, i):
                if i % j == 0:
                    break
                if j == i - 1:
                    Temp.append(i)
    else:
        Temp.append(2)
print(Temp)



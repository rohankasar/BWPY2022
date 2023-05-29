#Q40. Python program to check if a string is palindrome or not Reverse words in a given String in
data0 = 0
while data0 == 0:
    Data1 = input('Enter String :  ')
    Data2 = Data1[ : :-1]
    if Data1 == Data2:
        print("Origina String : ",Data1)
        print("Reverse String : ", Data2)
        print('String is palindrome')
    else:
        print("Origina String : ", Data1)
        print("Reverse String : ", Data2)
        print('String is not palindrome')
    while True:
        Data3 = input("Do you want to check next string [y/n] : ")
        if Data3 == 'y':
            break
        elif Data3 == 'n':
            data0 = 1
            break
        elif Data3 != 'y' or 'n':
            print("Enter Valid data ! ")
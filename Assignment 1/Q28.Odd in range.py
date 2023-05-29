#Q27. Python program to print all odd numbers in a range
while True :
    try:
        data1 =int(input("Enter range last Number : "))
        data2 = [ ]
        if data1%2 != 0:
            for x in range(data1+2):
                if x%2 != 0:
                    data2.append(x)
        else:
            for x in range(data1):
                if x%2 != 0:
                    data2.append(x)
        print(data2)
        print("Type Stop to end process ")
    except:
        break
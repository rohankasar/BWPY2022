#Q32. Python program to print all positive numbers in a range
while True :
    try:
        data1 =int(input("Enter range First Number : "))
        data3 = int(input("Enter range last Number : "))
        data2 = [ ]
        for x in range(data1,data3):
            if x  > 0:
                    data2.append(x)
        print(data2)
        print("Type Stop to end process ")
    except:
        break
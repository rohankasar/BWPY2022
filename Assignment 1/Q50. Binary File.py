#Q50. Python | Check if a given string is binary string or not

Data0 = input ("Enter String : ")
Data1 = 0
for x in Data0:
    try:
        if int(x) == 0 or 1:
            Data1 = 1
    except:
        print("String is Not binary  !!! ")
        Data1 = 0
        break
if Data1 == 1:
    print("String is binary  !!! ")

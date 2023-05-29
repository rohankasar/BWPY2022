#51. Python | Find all i q of input string from a list


Data = ''
Data0 = ''
Data1 = ''
def data():
    global Data
    global Data0
    global Data1
    Data = input("Enter List : ")
    Data0 = Data.split()
    # print(Data0) # To show list
   # Data1 = input('Enter the string which you want to match : ')

def match_Call():
    global Data
    global Data0
    global Data1
    data4 = 0
    Data1 = input('Enter the string which you want to match : ')
    for x in Data0:
        if Data1 in x:

            print(x ,   end = " , ")
            data4 = 1

    if data4 ==0:
        print("No match available . Try again ...!!! ")
print("GET WITH THE PROGRAM ...!!! ")

data()
match_Call()

while True:
    Data2 = (input("\n\nWhich Operation Do you want to perform ?\n 1. New Operation \n 2. Only check match string into existing \n 3. Exit All  \nPlease Select Option : "))
    #print(Data2)

    if Data2 == '1' :#or '1. new operation' or 'new nperation':
        data()
        match_Call()
    elif Data2 == '2' :#or '2. only check match string into existing' or 'only check match string into existing':
        match_Call()
    elif Data2 == '3' :#or '3. Exit All' or 'Exit All':
        print("\nThank You...!!!")
        break
    else :
        print("\nSelect correct option....!!!")



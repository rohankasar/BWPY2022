#Q1. Python Program for factorial of a number with and without recursion

def factorial():
    user_input = int(input("Enter Number : "))
    factorial = 1
    if user_input <= 0 or user_input==1:
        factorial = 1
        print(factorial)
    elif user_input > 1:
        for i in range(1,user_input+1):
            factorial = factorial*i
            i +=i
        print(factorial)
#----------------------------------------------------------
factorial()
while input("Do You Want To Continue? [y/n]: ") == "y":
    factorial()
else:
    print("Program End")



#========================

while True :
    while True:
        try:
            data = int(input("\nEnter Number : "))
            break
        except :
            print("Enter valid data...")

    def factt(data):
        if data > 0:
            facts = data * factt(data-1)
            return facts
        else:
            return 1
    print("Result : ",factt(data))

    d = input("Do you want to continue ?[y/n]")
    if d == 'n':
        print("Program end...")
        break
    else:
        print()
        pass




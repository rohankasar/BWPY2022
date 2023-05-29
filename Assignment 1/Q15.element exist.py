# # Q15 Ways to check if element exists in list
#
#  #program 1
# list1=[1,2,3,4,5,6]
# element = int(input("Enter Value : "))
# if element in  list1:
#     print("Correct Value")
# else:
#     print("Wrong  Value")

#  program  2
list1=[1,2,3,4,5,6,"ok"]
i = 0
#try :
while i == 0:
    element = eval(input("Enter Value : "))
    if element in  list1:
        print("Correct Value")
    else:
        print("Wrong  Value")
# except :
#     i = 1
#     print("Program Stop")
# #

#  program  3
# import ast
#
# list1=ast.literal_eval(input("Enter Element :"))
# print("Entered Elemet", list(list1))
# i = 0
# try :
#     while i == 0:
#         element = ast.literal_eval(input("Enter Value : "))
#         if element in  list1:
#             print("Correct Value")
#         else:
#             print("Wrong  Value")
#         print("To Exit to stop program")
#
# except :
#     i = 1
#     print("Program End")


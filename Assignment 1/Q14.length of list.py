#
# #Q14 . Ways to find length of list:
#
list1=[1,2,3,4,5,6]
#  program 1
print("Methode 1 Length : ", len(list1))

# program 2
count = 0
for i in list1:
    count += 1
print("Methode 2 Length : ",count)

#Discription : in first program i used length function to count length .
#                           in second program using for loop iteration find the length
# Output :
# Length : 6
# Length :  6
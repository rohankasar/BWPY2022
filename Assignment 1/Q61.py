#Q. Python program to find the sum of all items in a dictionary

# Hive Table = {
#   "a": 1,
#   "b": 2,
#   "c": 3,
#   "d": 4,
#   "e": 5,
#   "f": 5
# }
#
# x = Hive Table.values()
# print(x)
#
# sum = 0
# for i in x:
#   sum = i + sum
#
# print("sum : ", sum)
#
# # using indexing
#
# y = list(Hive Table.values())
# print(y)
#
# sum = 0
# for j in range(len(y)):
#   sum = y[j] + sum
#
# print("sum : ", sum)

#========================================
Data = {
  "a": 1,
  "b": "Rohan",
  "c": 3,
  "d": 4,
  "e": "Kasar",
  "f": 5,
  "g": 2.2,
  "h" : 5.2
}

x = Data.values()
print(x)

sum = 0
sum2 = ""
sum3 = 0.0
for i in x:
  if type(i) == int:
    sum = i + sum

  elif type(i) == str:
    sum2 = sum2 +" " + i

  else:
    sum3 = i + sum3

print("\nint sum :" ,sum)
print("\nstring is :",sum2)
print("\nfloat sum : ",sum3)

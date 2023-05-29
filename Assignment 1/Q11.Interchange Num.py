#Q11. Python program to interchange first and last elements

# data = eval(input('Enter Elements :  '))
#
# data[0], data[-1] = data[-1], data[0]
# print('Result : ',data)
#

data = [1,2,3,4,5,6,7]
l = len(data)
data2 = []
for i in range(l):
    if i > 1 and i < l:
        data2.append(i)
    if i == 0:
        x = data[i]
    if i == l-1:
        y = data[i]

data2.insert(0,y)
data2.insert(l,x)
print(data2)

# data = [1,2,3,4,5,6,7]
# d2 = []
# d3 = []
# d4 = []
# for i in range(len(data)):
#     if i == 0:
#         d4.append(data[0])
#     elif i == len(data) - 1:
#         d2.append(data[len(data)-1])
#     else:
#         d3.append(data[i])
# print(d2 + d3 + d4)


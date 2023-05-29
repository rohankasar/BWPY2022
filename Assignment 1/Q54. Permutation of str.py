#Q54. Python | Permutation of a given string using inbuilt function
data = "123"
print("Using nested for loop :")
for i in data:
    for j in data:
        for k in data:
            if i != j and i != k and j!=k:
                print(i,j,k)

#======================================================

print("\nUsing List comprehension :")
data2 = [print(x,y,z) for x in data for y in data for z in data if x != y and x != z and y != z ]

#Q36. Python | Remove empty tuples from a list

Data1 = [1,(),2,(),3,(),4]

for i in Data1:
    if i == ():
        Data1.remove(())
print(Data1)
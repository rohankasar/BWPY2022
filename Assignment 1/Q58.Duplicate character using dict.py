# Q58 Python Counter| Find all duplicate characters in string Dictionary Programs:

data = "abcdabcdadcccbbbcc"
dct = dict()

for i in data:
    if i not in dct.keys():
        dct[i] = 1
        print(i,end=",")
    else:
        dct[i] += 1

print("\n\n",dct)
# 64. Python | Merging two Dictionaries Program to create grade calculator in Python
"""  "score > 90" : "A",
    "score > 80" : "B",
    "score > 70" : "C"
"""
dct1 = {
    "Name " :  "Rohan",
    "Marks ": [55,65,70,47]
}
dct2 = {
    "Name " :  "Kajal",
    "Marks ": [80,75,80,77]
}
dct3 = {
    "Name " :  "RK",
    "Marks ": [60,85,85,77]
}
#
x = list(dct1.values())
print(x)

avg = 0
sum = 0
for i in x:
    if type(i) == int:
        sum = sum + i
        avg = sum


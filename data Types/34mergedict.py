mydict1 = {}
mydict2 = {}

for i in range(1, 7):
    mydict1[i] = i*i
    mydict2[i] = i+i+i
print(mydict1)
print(mydict2)


mydict1.update(mydict2)
print(mydict1)

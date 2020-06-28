mydict1 = {}
size = int(input("size:"))
for i in range(size):
    mydict1[i] = i*i
print(mydict1)
result = sum(mydict1.values())
print(result)

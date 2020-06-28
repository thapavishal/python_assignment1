lis = []

size = int(input("Enter the size :"))

for i in range(size):

    nameList = input("Enter the string: ")
    lis.append(nameList)
print(lis)

count = 0
for name in lis:
    print(name)
    if len(name) > 1 and name[0] == name[-1]:
        count += 1
print(count)

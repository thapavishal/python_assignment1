lst = []

size = int(input("Enter the size of the list: "))
print(size)

for el in range(size):
    numb = int(input("Enter number: "))
    lst.append(numb)
print(lst)

mul = 1
for el in range(size):
    mul *= lst[el]
print(mul)

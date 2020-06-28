lst = []

size = int(input("Enter the size of the list: "))
print(size)

for el in range(size):
    element = int(input("Enter number: "))
    lst.append(element)
print(lst)

b = set()
unique = []
for el in lst:
    if el not in b:
        unique.append(el)
        b.add(el)

print("Unique elements: ", unique)

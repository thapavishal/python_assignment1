lst = []

size = int(input("Enter the size of the list: "))
print(size)

for i in range(size):
    numb = int(input("Enter number: "))
    lst.append(numb)
print("Unsorted numbers: ", lst)

lst.sort()
print("sorted List: ", lst)
print("Largest number:", lst[i])

dict1 = {}

size = int(input("Enter the size of the list: "))
print(size)

for i in range(size):
    key = input("Enter the key: ")
    value = input("Enter the value:")

    dict1.update({key: value})
    print("New Dictionary:", dict1)

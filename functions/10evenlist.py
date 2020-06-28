
def even():
    data = []
    n = int(input("Enter the size of the list:"))

    list2 = []
    for el in range(n):
        el = int(input("Enter the element:"))
        data.append(el)
    print("raw list:", data)

    for el in data:
        if el % 2 == 0:
            list2.append(el)
    print("The list of even number is: ", list2)


even()

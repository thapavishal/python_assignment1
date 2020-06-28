list1 = print(list(range(10)))

a = input("Enter the number: ")
print(a)


def find_num(a):
    for el in list1:
        if a not in list1:
            print("No")
        else:
            list1[el]
            print("The number is in the list")


print("The result:", find_num(a))

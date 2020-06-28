list1 = []
list2 = []


def uniq():
    for num in range(0, 9):
        num = input("Enter the number: ")
        list1.append(num)
    print(list1)

    for a in list1:
        if a not in list2:
            list2.append(a)
        list2.sort()
    print(list2)

    return


uniq()

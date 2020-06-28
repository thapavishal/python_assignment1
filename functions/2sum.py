lst = []

size = int(input("Enter the size of the list: "))
print(size)


def add():
    sum = 0
    for ele in range(size):
        ele = int(input("Enter number: "))
        lst.append(ele)
        sum += ele
    return sum


print("sum : ", add())

container = []

size = int(input("Enter the size:"))
print(size)


def mul_num():
    product = 1
    for num in range(size):
        num = int(input("Enter number: "))
        container.append(num)
        product = product * num
    return product


print(" The product of the numbers: ", mul_num())

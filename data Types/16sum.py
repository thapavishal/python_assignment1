
lst = []
num = int(input("size:"))
for i in range(num):
    res = int(input("Enter number:"))
    lst.append(res)
    # print(lst)
print(lst)

sum = 0
for i in range(num):
    sum += lst[i]
print(sum)


# second method
"""
list1 = [10, 20, 30, 40]

total = 0
for i in range(0, len(list1)):
    total += list1[i]
print(total)
"""

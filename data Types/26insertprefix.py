list1 = [1, 2, 3, 4]
str1 = 'emp'

str1 += '{0}'

for i in list1:
    list2 = str1.format(i)

print(list2)

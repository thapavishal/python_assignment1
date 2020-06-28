list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
a = sorted(list1)
print("Sorted list based on first element:", a)


def secondValue(element):
    return element[1]


result = sorted(list1, key=secondValue)
print("Sorted list based on second element: ", result)


# sorting tuple
"""
tuple1 = ((2, 5), (1, 2), (4, 4), (2, 3), (2, 1))
a = sorted(tuple1)
print("Sorted tuple based on first element:", a)


def secondValue(element):
    return element[1]


result = sorted(tuple1, key=secondValue)
print("Sorted tuple based on second element", result)

"""

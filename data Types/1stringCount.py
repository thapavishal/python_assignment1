
mystr = input("Enter the string: ")
print(len(mystr))


countDict = {}

for i in mystr:
    if i in countDict.keys():
        countDict[i] += 1  # increase the counter for the letters that repeats
    else:
        # the letters that comes for the first time set the counter to 1
        countDict[i] = 1
print(countDict)


# Second method using count function
"""
mystr = input("Enter the string: ")
print(len(mystr))
dictionary = {}
for i in mystr:
    dictionary[i] = mystr.count(i)
print(dictionary)
"""

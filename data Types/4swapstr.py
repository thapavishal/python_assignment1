
firststr = input("Enter first string: ")
secondstr = input("Enter second string: ")

new_firststr = secondstr[:2] + firststr[2:]
new_secondstr = firststr[:2] + secondstr[2:]

result = new_firststr + ' ' + new_secondstr
print(result)

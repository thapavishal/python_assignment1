"""
def func_max(a, b, c):
    data = [a, b, c]
    return max(data)


x = int(input("Enter first number: "))
y = int(input("Enter Second number: "))
z = int(input("Enter third number: "))

print("Max number is: ", func_max(x, y, z))
"""


def max_num(firstnumber, secondnumber, thirdnumber):
    if(firstnumber >= secondnumber) and (firstnumber >= thirdnumber):
        large = firstnumber
    elif (secondnumber >= thirdnumber) and (secondnumber >= firstnumber):
        large = secondnumber
    else:
        large = thirdnumber

    return large


x = int(input("Enter first number: "))
y = int(input("Enter Second number: "))
z = int(input("Enter third number: "))

print("Max number is: ", max_num(x, y, z))

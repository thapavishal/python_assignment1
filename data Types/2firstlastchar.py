
def add_string(n):
    if len(n) < 2:
        return ''
    else:
        return n[:2] + n[-2:]


strcon = input("Enter the string: ")
result = add_string(strcon)
print(result)

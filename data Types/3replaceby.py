"""
lis = []
s = input("Enter String : ")
for ch in s:
    if ch in lis:
        lis.append('$')
    else:
        lis.append(ch)
print(''.join(str(i) for i in lis))
"""


def replace_dubli(mystr):
    name = mystr[0]
    mystr = mystr.replace(name, '$')
    mystr = name + mystr[1:]
    return mystr


userstr = input("Enter the string: ")
result = replace_dubli(userstr)
print(result)

def add_ing(str):
    if len(str) >= 3:
        if str.endswith('ing'):
            str += 'ly'
        else:
            str += 'ing'
    return str


string1 = input("Enter any string: ")
new_string = add_ing(string1)

print(new_string)

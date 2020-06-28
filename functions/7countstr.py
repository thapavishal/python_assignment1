

def count_ul(name):
    upper = lower = 0

    for i in name:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print("Upper count:", upper)
    print("lower count:", lower)
    return


name = str(input("Enter the string: "))
count_ul(name)


def fact(n):
    facto = 1

    for i in range(1, n+1):
        facto = facto*i
    return facto


n = int(input("Enter the number: "))

print("The factorial of the number is: ", fact(n))

chris = {}

n = int(input("Enter the size:"))
result = 1
for i in range(1, n+1):
    chris[i] = i+i
    result = result * chris[i]

print("The dictionary is: ", chris)
print("The result after multiplication: ", result)

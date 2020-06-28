mystr = input("Enter comma seperated strings:")
print("Input String:", mystr)

comma_mystr = mystr.split(",")
result = sorted(comma_mystr)
print(",".join(result))

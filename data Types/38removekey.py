dict1 = {1: 'Apple', 2: 'Chris', 3: 'Thor',
         4: 'Strange', 5: 'Doctor', 6: 'Shiva'}
s = int(input("Please enter the key that you want to Delete : "))
if s in dict1:
    del dict1[s]
else:
    print("Wrong key, choose from dictionary")

print("New dictionary:", dict1)

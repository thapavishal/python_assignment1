name = "hello"
new = ""
n = len(name)
new += name[n-1]

i = 1
while(i < n-1):
    new += name[i]
    i = i+1

new += name[0]
print(new)

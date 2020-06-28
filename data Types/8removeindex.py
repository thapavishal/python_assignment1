mystr = "Kathmandu"
index = 5
n = len(mystr)
new_str = ""
i = 0

while(i < n):
    if(i != index):
        new_str += mystr[i]
    i = i+1
print(new_str)

# second method using function
"""
mystr = "Trondheim"
print(mystr)

def remove_str(mystr, n):
     return mystr[:n] + mystr[n+1:]
    
new_string = remove_str(mystr, 6)
print(new_string)
"""

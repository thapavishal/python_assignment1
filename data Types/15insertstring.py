def insert_string(mystr, message):
    return mystr[:2] + message + mystr[2:]


user_message = input("Enter the message: ")
print(user_message)
result = insert_string('[[]]', user_message)

print(result)

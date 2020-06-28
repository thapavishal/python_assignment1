mystr = input("Enter the message: ")

message = mystr.split()
wordDict = {}
for el in message:
    if el not in wordDict.keys():
        wordDict[el] = 0
    wordDict[el] += 1
print(wordDict)

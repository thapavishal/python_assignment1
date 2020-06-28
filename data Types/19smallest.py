numList = []

size = int(input("Enter the size of the list: "))
print(size)

for i in range(size):
    num = int(input("Enter the number: "))
    numList.append(num)
print("Unsorted List: ", numList)

numList.sort()
# numList.sort(reverse=True)  # for descending order
print("Sorted List: ", numList)
print("Smallest number: ", numList[0])

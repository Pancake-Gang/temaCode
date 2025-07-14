array = [3, 4, 3, 2, 2, 1, 2, 5, 3, 4, 1, 2, 5, 2, 3, 3, 1, 4, 3, 1, 2, 5, 4, 2]

array.sort()

count = 1
highestCount = 1
mostFrequent = array[0]
currentNumber = array[0]

for i in range(1, len(array) - 1):
    if array[i] == currentNumber:
        count += 1
        if count > highestCount:
            highestCount = count
            mostFrequent = currentNumber
    else:
        count = 1
        currentNumber = array[i]


print(mostFrequent, highestCount)

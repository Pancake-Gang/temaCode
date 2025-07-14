num = 2**1000
stringNum = str(num)
summation = 0

for i in range(len(stringNum)):
    digit = int(stringNum[i])
    summation += digit

print(summation)

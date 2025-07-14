num = 100

sumOfSquare = 0
squareOfSum = ((num/2) * (num + 1))**2

for i in range(1, num + 1):
    sumOfSquare += i**2

value = squareOfSum - sumOfSquare
print(int(value))


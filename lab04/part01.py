# 04.1.1 Integer numbers.
"""
numOfNumber = int(input("Please enter a number for numbers: "))
x = 0
numbers = []
subNumbers = []
while x < numOfNumber:
    number = int(input("Please enter a number: "))
    if x > 0:
        subNumber = numbers[-1] + number
        subNumbers.append(subNumber)
    numbers.append(number)
    x += 1

print(numbers)
y = 0
while y < numOfNumber-1:
    if y != len(numbers):
        firstValue = numbers[y]
        y += 1
        secondValue = numbers[y]
        sumTotal = firstValue + secondValue
        print(sumTotal)
"""
# 04.1.2 String analysis.

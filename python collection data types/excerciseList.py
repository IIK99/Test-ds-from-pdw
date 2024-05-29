# Find min and max values in numbers
numbers = [41, 5, 1, 3, 89, 32]

# Initialize min and max
minValue = numbers[0]
maxValue = numbers[0]

# Find min
for number in numbers:
    if number < minValue:
        minValue = number

print("Min:", minValue)

# Find max
for number in numbers:
    if number > maxValue:
        maxValue = number

print("Max:", maxValue)

print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

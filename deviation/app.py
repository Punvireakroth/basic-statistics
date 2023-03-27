numbers = [1, 2, 3, 4, 5]

# calculate mean
mean = sum(numbers) / len(numbers)

# calculate deviation from mean for each number
deviations = []
for number in numbers:
    deviation = number - mean
    deviations.append(deviation)

print(deviations)
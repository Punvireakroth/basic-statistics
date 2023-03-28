import numpy as np

# data
year = list(range(2006, 2016))
heart_transplants = [2193, 2209, 2163, 2211, 2332, 2322, 2378, 2531, 2655, 2804]

# means
x_mean = np.mean(year)
y_mean = np.mean(heart_transplants)

# slope
numerator = sum([(year[i] - x_mean) * (heart_transplants[i] - y_mean) for i in range(len(year))])
denominator = sum([(year[i] - x_mean)**2 for i in range(len(year))])
slope = numerator / denominator

# Calculate the y-intercept
y_intercept = y_mean - slope * x_mean

# result
equation = f'y = {slope:.2f}x + {y_intercept:.2f}'

print(equation)

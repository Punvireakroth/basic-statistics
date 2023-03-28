import math

# Given data
x = [0.2, 0.5, -0.1, 1.4, 1.1, 0.8, -0.2, -0.9, -1.3, -0.5, -1.1, -1.4]
y = [4, 7, 6, 15, 12, 10, 6, 3, 2, 5, 1, 0]

# Sample means and standard deviations
x_mean = sum(x) / len(x)
y_mean = sum(y) / len(y)
x_stddev = math.sqrt(sum([(i - x_mean)**2 for i in x]) / (len(x) - 1))
y_stddev = math.sqrt(sum([(i - y_mean)**2 for i in y]) / (len(y) - 1))

# Sample correlation coefficient
r = sum([(x[i] - x_mean) * (y[i] - y_mean) for i in range(len(x))]) / ((len(x) - 1) * x_stddev * y_stddev)

# Slope and intercept of least-squares line
b = r * (y_stddev / x_stddev)
a = y_mean - b * x_mean

# Equation of least-squares line
print("---------------------------------")
print("y = {:.3f}x + {:.3f}".format(b, a))
print("---------------------------------")

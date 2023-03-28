import numpy as np

# Input data
x = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
y = np.array([33.3, 58.3, 81.8, 96.7, 100.0])

# Transform x
x_prime = np.sqrt(x)

# Calculate slope and intercept of least-squares line
n = len(x_prime)
slope = (n*np.sum(x_prime*y) - np.sum(x_prime)*np.sum(y)) / (n*np.sum(x_prime**2) - np.sum(x_prime)**2)
intercept = np.mean(y) - slope*np.mean(x_prime)

# Print equation of line
print(f"y = {slope:.3f}x' + {intercept:.3f}")

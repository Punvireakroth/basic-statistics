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

# Make predictions
x1 = 1.75 * np.sqrt(x[0])  # Energy of shock 1.75 times the threshold level
x2 = 0.8 * np.sqrt(x[0])   # Energy of shock 0.8 times the threshold level
y1 = slope*x1 + intercept   # Predicted success for x1
y2 = slope*x2 + intercept   # Predicted success for x2

# Print predictions
print(f"Predicted success for energy of shock 1.75 times the threshold level: {y1:.1f}%")
print(f"Predicted success for energy of shock 0.8 times the threshold level: {y2:.1f}%")

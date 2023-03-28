import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
y = np.array([33.3, 58.3, 81.8, 96.7, 100.0])

# Fit a least-squares line
a, b = np.polyfit(x, y, 1)

# Construct a scatterplot and least-squares line
plt.scatter(x, y)
plt.plot(x, a*x + b, color='red')
plt.xlabel('Energy of Shock')
plt.ylabel('Success (%)')
plt.show()


import numpy as np

x = [23, 14, 14, 0, 17, 20, 20, 15, 21]
y = [43, 59, 48, 77, 50, 52, 46, 51, 51]


r = np.corrcoef(x, y)[0, 1]
print(f"The correlation coefficient is {r:.3f}")
import matplotlib.pyplot as plt

year = list(range(2006, 2016))
heart_transplants = [2193, 2209, 2163, 2211, 2332, 2322, 2378, 2531, 2655, 2804]

plt.scatter(year, heart_transplants)
plt.xlabel('Year')
plt.ylabel('Number of Heart Transplants')
plt.title('Scatterplot of Heart Transplants from 2006 to 2015')
plt.show()

import matplotlib.pyplot as plt

x = [0.5, 1.0, 1.5, 2.0, 2.5]
y = [33.3, 58.3, 81.8, 96.7, 100.0]

plt.scatter(x, y)
plt.xlabel('Energy of Shock')
plt.ylabel('Success (%)')
plt.show()

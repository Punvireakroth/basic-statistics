import matplotlib.pyplot as plt

x = [23, 14, 14, 0, 17, 20, 20, 15, 21]
y = [43, 59, 48, 77, 50, 52, 46, 51, 51]

plt.scatter(x, y)
plt.title('Test Anxiety vs. Exam Scores')
plt.xlabel('Test Anxiety Score')
plt.ylabel('Exam Score')
plt.show()

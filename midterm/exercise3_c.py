import matplotlib.pyplot as plt

# Define the data
year = list(range(2006, 2016))
heart_transplants = [2193, 2209, 2163, 2211, 2332, 2322, 2378, 2531, 2655, 2804]

# Calculate the means of year and heart_transplants
mean_year = sum(year) / len(year)
mean_heart_transplants = sum(heart_transplants) / len(heart_transplants)

# Calculate the slope and y-intercept of the regression line
numerator = 0
denominator = 0
for i in range(len(year)):
    numerator += (year[i] - mean_year) * (heart_transplants[i] - mean_heart_transplants)
    denominator += (year[i] - mean_year)**2

slope = numerator / denominator
y_intercept = mean_heart_transplants - slope * mean_year

# Construct the regression line
regression_line = []
for i in year:
    regression_line.append(slope * i + y_intercept)

# Calculate the residuals
residuals = []
for i in range(len(year)):
    residuals.append(heart_transplants[i] - regression_line[i])

print(residuals)

# Plot the residuals
plt.scatter(year, residuals)
plt.axhline(y=0, color='r', linestyle='-')
plt.xlabel('Year')
plt.ylabel('Residuals')
plt.title('Residual Plot for Heart Transplant Data')
plt.show()

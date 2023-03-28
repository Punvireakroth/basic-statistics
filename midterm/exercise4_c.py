
# Import numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the original data
x = np.array([0.5,1.0,1.5,2.0,2.5])
y = np.array([33.3,58.3,81.8,96.7,100])

# Define the transformed data
x_prime = np.sqrt(x)
x_double_prime = np.log(x)

# Define a function to calculate the slope and intercept of a least-squares line
def least_squares(x,y):
  n = len(x)
  sum_x = np.sum(x)
  sum_y = np.sum(y)
  sum_xy = np.sum(x*y)
  sum_x2 = np.sum(x**2)
  slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
  intercept = (sum_y - slope * sum_x) / n
  return slope, intercept

# Define a function to calculate the residuals for a given model
def residuals(x,y,slope,intercept):
  y_pred = slope * x + intercept
  res = y - y_pred
  return res

# Define a function to plot a scatter plot and a least-squares line
def scatter_plot(x,y,slope,intercept,title):
  plt.scatter(x,y,color='blue',label='Data')
  plt.plot(x,slope*x+intercept,color='red',label='Least-squares line')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title(title)
  plt.legend()
  plt.show()

# Define a function to plot a residual plot
def residual_plot(x,res,title):
  plt.scatter(x,res,color='green',label='Residuals')
  plt.axhline(y=0,color='black',label='Zero line')
  plt.xlabel('x')
  plt.ylabel('Residuals')
  plt.title(title)
  plt.legend()
  plt.show()

# Calculate the slope and intercept for the original data
m,b = least_squares(x,y)

# Plot the scatter plot and the least-squares line for the original data
scatter_plot(x,y,m,b,'Original data')

# Calculate the residuals for the original data
res = residuals(x,y,m,b)

# Plot the residual plot for the original data
residual_plot(x,res,'Residual plot for original data')

# Calculate the slope and intercept for the transformed data using x' = sqrt(x)
m_prime,b_prime = least_squares(x_prime,y)

# Plot the scatter plot and the least-squares line for the transformed data using x' = sqrt(x)
scatter_plot(x_prime,y,m_prime,b_prime,"Transformed data using x' = sqrt(x)")

# Calculate the residuals for the transformed data using x' = sqrt(x)
res_prime = residuals(x_prime,y,m_prime,b_prime)

# Plot the residual plot for the transformed data using x' = sqrt(x)
residual_plot(x_prime,res_prime,"Residual plot for transformed data using x' = sqrt(x)")

# Calculate the slope and intercept for the transformed data using x'' = ln(x)
m_double_prime,b_double_prime = least_squares(x_double_prime,y)

# Plot the scatter plot and the least-squares line for the transformed data using x'' = ln(x)
scatter_plot(x_double_prime,y,m_double_prime,b_double_prime,"Transformed data using x'' = ln(x)")

# Calculate the residuals for the transformed data using x'' = ln(x)
res_double_prime = residuals(x_double_prime,y,m_double_prime,b_double_prime)

# Plot the residual plot for the transformed data using x'' = ln(x)
residual_plot(x_double_prime,res_double_prime,"Residual plot for transformed data using x'' = ln(x)")
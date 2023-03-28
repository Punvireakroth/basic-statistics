import numpy as np

# dataset
BMI_change = np.array([0.5,-0.5,0.0,0.1,0.7,0.8,1.0,1.5,1.1,1.0,0.3,0.3])
depression_score_change = np.array([-1,9,4,4,6,7,13,14,17,18,12,14])

# Find slope intercept line and mean 
x_mean = np.mean(BMI_change)
y_mean = np.mean(depression_score_change)

numerator = np.sum((BMI_change - x_mean) * (depression_score_change - y_mean))
denominator = np.sum((BMI_change - x_mean) ** 2)

slope = numerator / denominator
intercept = y_mean - slope*x_mean

line = slope*BMI_change + intercept

# Calculating r2 and se
correlation_matrix = np.corrcoef(BMI_change, depression_score_change)
r_value = correlation_matrix[0, 1]
r2 = r_value**2

se = np.sqrt(np.sum((depression_score_change - line)**2)/(len(BMI_change)-2))

# Printing the results
print("r2 = {:.3f}".format(r2))
print("se = {:.3f}".format(se))

# Conclusion
if r2 > 0.5 and se < 2:
    print("The least square line does a good job of describing the relationship between change in depression score and change in BMI.")
else:
    print("The least square line does not do a good job of describing the relationship between change in depression score and change in BMI.")

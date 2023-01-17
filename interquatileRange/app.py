import pandas as pd
numbers = [1, 2, 3, 4, 5]

# calculate quartiles
q1 = pd.Series(numbers).quantile(0.25)
q3 = pd.Series(numbers).quantile(0.75)

# calculate interquartile range
iqr = q3 - q1

print(iqr)


def mean(values):
    return sum(values) / len(values)

def standard_deviation(values):
    number_of_values = len(values)
    mean_of_values = mean(values)
    return (sum((value - mean_of_values) ** 2 for value in values) / number_of_values) ** 0.5

def correlation_coefficient(list_x, list_y):
    number_of_values = len(list_x)
    mean_of_list_x = mean(list_x)
    mean_of_list_y = mean(list_y) 
    
    standard_deviation_of_list_x = standard_deviation(list_x)
    standard_deviation_of_list_y = standard_deviation(list_y)
    
    covariance = 0

    for i in range(number_of_values):
        covariance += (list_x[i] - mean_of_list_x) * (list_y[i] - mean_of_list_y)
    covariance /= number_of_values
    
    correlation_coefficient = covariance / (standard_deviation_of_list_x * standard_deviation_of_list_y)
    
    return correlation_coefficient

x = [2.3,2.3,2.35,2.4,2.4,2.6,2.68,2.7]
y = [43,8,41,53,35,55,20,11]

#function call
print(abs(correlation_coefficient(x, y)))
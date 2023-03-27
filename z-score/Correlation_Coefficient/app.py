import statistics as stats

def correlation_coefficient(x, y):
    n = len(x)
    
    # Calculate the means of x and y
    x_mean = stats.mean(x)
    y_mean = stats.mean(y)
    
    # Calculate the standard deviations of x and y
    x_stddev = stats.stdev(x)
    y_stddev = stats.stdev(y)
    
    # Calculate the covariance
    cov = 0
    for i in range(n):
        cov += (x[i] - x_mean) * (y[i] - y_mean)
    cov /= n
    
    # Calculate the correlation coefficient

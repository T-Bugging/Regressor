import matplotlib.pyplot as plt;

dev_x = [ 1,20,100,1,500]
dev_y = [ 1,2, 1.5 ,3 , 2.5 ]

def linear_regg(arr1,arr2):
    n = len(arr1)
    sum_xy = sum([x * y for x, y in zip(arr1, arr2)])
    sum_x = sum(arr1)
    sum_y = sum(arr2)
    sum_xx= sum([x * y for x, y in zip(arr1,arr1)])

    slope = ((n*sum_xy) -(sum_x * sum_y)) /((n * sum_xx) - (sum_x*sum_x))  
    intercept = (sum_y - (slope * sum_x )) / n
    return slope, intercept 


slope , intercept = linear_regg(dev_x,dev_y)
 
y= [slope * x + intercept for x in dev_x]

plt.scatter(dev_x, dev_y)

# Plot the regression line
plt.plot(dev_x, y)

# Add labels, legend, and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Linear Regression Line')


# Display the plot
plt.show()

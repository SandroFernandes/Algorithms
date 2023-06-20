import matplotlib.pyplot as plt
import numpy as np

# Time complexities and their labels
complexities = ['O(1)', 'O(n)', 'O(n^2)', 'O(n^3)', 'O(log n)', 'O(n log n)', 'O(n^c)', 'O(c^n)', 'O(n!)']
labels = ['Constant Time', 'Linear Time', 'Quadratic Time', 'Cubic Time', 'Logarithmic Time', 'Linearithmic Time',
          'Polynomial Time', 'Exponential Time', 'Factorial Time']

# Number of data points
n = len(complexities)

# Assign x-axis values (input size)
x = np.arange(1, 10, 0.1)  # Adjust the range and step size as needed

# Plot each line for the time complexities
for i in range(n):
    y = np.power(x, i + 1)  # Replace with the desired time complexity function
    plt.plot(x, y, label=labels[i])

# Set the x-axis label
plt.xlabel('Input Size (n)')

# Set the y-axis label
plt.ylabel('Number of Operations (N)')

# Set the chart title
plt.title('Time Complexities')

# Adjust the y-axis limits for a larger scale
plt.ylim(0, 100)  # Adjust the upper limit as needed

# Add a legend
plt.legend()

# Display the chart
plt.show()

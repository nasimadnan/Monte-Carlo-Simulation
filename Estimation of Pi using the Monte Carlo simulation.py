import math
import random
import numpy as np
import matplotlib.pyplot as plt

total_points = 10000

circle_points = 0
square_points = 0

# Create an empty plot
fig, ax = plt.subplots()

# Set the x-axis and y-axis limits in the plot
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

for i in range(total_points):

    # Generate a point (x, y)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # Distance of (x, y) from the origin
    dist = x**2 + y**2
 
    # Checking if (x, y) is inside the circle
    if dist <= 1:
        circle_points += 1
        ax.scatter(x*100,y*100,color = 'red')
    else:
        ax.scatter(x*100,y*100,color = 'blue')

    square_points += 1
 
    # pi = 4 * probability of (x, y) is inside the circle

    pi = 4 * circle_points / square_points

    # Dynamic outputs
    ax.set_title('Estimation of Pi using the Monte Carlo simulation')
    ax.set_xlabel('Current value of Pi: ' + str(pi))
    ax.set_ylabel('Current number of point: ' + str(i+1))

    plt.pause(0.00001)

print('Thank You')

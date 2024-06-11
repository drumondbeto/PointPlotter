import json
import matplotlib.pyplot as plt

# Toggle labels visibility
showLabels: bool = True 

# Load data from JSON file
with open('2D_Points.json', 'r') as f:
    points = json.load(f)

# Set up point coordinates
x, y = zip(*points)

# Plot points on the graph
plt.scatter(x, y)

# Set up labels if enabled
if showLabels:
    labels = [f'P{i+1}' for i in range(len(x))]
    for i, txt in enumerate(labels):
        plt.annotate(txt, (x[i], y[i]))

# Display the plot
plt.show()

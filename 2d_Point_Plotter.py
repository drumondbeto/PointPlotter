import matplotlib.pyplot as plt
import json

# Show/Hide labels
showLabels: bool = True 

# Retrieve data
with open('2D_Points.json', 'r') as f:
    data = json.load(f)

# Set up points coords
x = data["x"]
y = data["y"]

# Plot points
plt.scatter(x, y)

# Set up labels
if showLabels:
    labels = [f'P{i+1}' for i in range(len(x))]
    for i, txt in enumerate(labels):
        plt.annotate(txt, (x[i], y[i]))

# Show graphics
plt.show()
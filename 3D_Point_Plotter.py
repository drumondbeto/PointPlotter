import json
import matplotlib.pyplot as plt

# Toggle labels visibility
showLabels: bool = True 
# Toggle axis proportions
staticAxisProportions: bool = False 

# Load data from a JSON file
with open('3D_Points.json', 'r') as f:
    points = json.load(f)

# Create and set up 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract X, Y, and Z point coordinates
x, y, z = zip(*points)

# Plot points
ax.scatter(x, y, z, color='blue')

# Set up labels if enabled
if showLabels:
    labels = [f'P{i+1}' for i in range(len(x))]
    for i, label in enumerate(labels):
        ax.text(x[i], y[i], z[i], label)

# Fix axis proportions
if staticAxisProportions:
    plt.axis('equal')

# Display the plot
plt.show()
# 2D and 3D Point Plotter

This project includes two Python scripts that visualize point data in both 2D and 3D space. The scripts leverage the `matplotlib` library to create plots, allowing for visual analysis of datasets.

## Features

- **2D Point Plotter**: Plots a set of 2D points from a JSON file and can toggle labels for each point.
- **3D Point Plotter**: Extends the plotting to three dimensions, also reading from a JSON file, with options to toggle labels and adjust axis proportions.

## Dependencies

- Python 3.x
- Matplotlib
- JSON

Ensure you have Python installed, along with the Matplotlib library, which can be installed via pip:

pip install matplotlib

## Data Format
The data for the plots is expected in JSON format. Example structures for the input data:

### 2D Points: Stored in 2D_Points.json

[
  [x1, y1],
  [x2, y2],
  ...
]

### 3D Points: Stored in 3D_Points.json

[
  [x1, y1, z1],
  [x2, y2, z2],
  ...
]

## Usage
To run the scripts, navigate to the directory containing the scripts and execute them with Python:

python 2D_Point_Plotter.py
python 3D_Point_Plotter.py

## Visualizing Points
Upon execution, the scripts will display the plots with the points loaded from the corresponding JSON files. Labels and axis proportions can be adjusted within the script files.

## Contributions
Contributions are welcome. Please open an issue to propose changes or submit a pull request.

## License
This project is open-sourced under the MIT license.

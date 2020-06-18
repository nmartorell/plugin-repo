import dataiku
from dataiku.customrecipe import *
import pandas as pd, numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os


### READ PLUGIN INPUTS ###

# Retrieve input and output dataset names
input_dataset_name = get_input_names_for_role('input_dataset')[0]
output_folder_name = get_output_names_for_role('main_output')[0]

# Retrieve mandatory user-defined parameters
plot_title = get_recipe_config().get('plot_title', "Scatter Plot Title")
    
x_axis = get_recipe_config().get('x_axis', None)
y_axis = get_recipe_config().get('y_axis', None)
z_axis = get_recipe_config().get('z_axis', None)

# Retrieve optional user-defined parameters
filter_column = get_recipe_config().get('filter_column', None)
filter_value = get_recipe_config().get('filter_value', None)
    
# Read input dataset as dataframe
input_dataset = dataiku.Dataset(input_dataset_name)
df = input_dataset.get_dataframe()


### ERROR CHECKING OF USER INPUTS ###

# Check that x, y and z axis correspond to column names
if (x_axis not in df.columns) or (y_axis not in df.columns) or (z_axis not in df.columns):
    raise KeyError("X-, Y-, and Z-axis parameters must be columns in the input dataset")

### GENERATE 3D SCATTER PLOT ###

# Filter values in dataset (optional, based in user input)
if (filter_column != "") and (filter_column != None):
    df = df[df[filter_column] == filter_value]

# Determine average z-axis value, for overlapping x-axis and y-axis values
df_avg_purchase = df[[x_axis, y_axis, z_axis]].groupby(by=[x_axis, y_axis], as_index=False).mean()

# Construct scatter plot 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs = df_avg_purchase[x_axis]
ys = df_avg_purchase[y_axis]
zs = df_avg_purchase[z_axis]

ax.set_xlabel(x_axis)
ax.set_ylabel(y_axis)
ax.set_zlabel(z_axis)
ax.set_title(plot_title)

ax.scatter(xs, ys, zs)


### SAVE SCATTER PLOT TO FOLDER ###

folder_for_plots = dataiku.Folder(output_folder_name)
folder_path = folder_for_plots.get_path()

path_fig = os.path.join(folder_path, plot_title)
plt.savefig(path_fig)
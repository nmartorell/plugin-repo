import dataiku
from dataiku.customrecipe import *

# Retrieve input and output datasets
input_dataset = get_input_names_for_role('input_dataset')[0]
output_dataset = get_output_names_for_role('main_output')[0]

# Retrieve user-defined parameters
plot_title = get_recipe_config()['plot_title']

x_axis = get_recipe_config()['x_axis']
y_axis = get_recipe_config()['y_axis']
z_axis = get_recipe_config()['z_axis']




# The configuration consists of the parameters set up by the user in the recipe Settings tab.

# Parameters must be added to the recipe.json file so that DSS can prompt the user for values in
# the Settings tab of the recipe. The field "params" holds a list of all the params for wich the
# user will be prompted for values.

# The configuration is simply a map of parameters, and retrieving the value of one of them is simply:
my_variable = get_recipe_config()['parameter_name']

# For optional parameters, you should provide a default value in case the parameter is not present:
my_variable = get_recipe_config().get('parameter_name', None)

# Note about typing:
# The configuration of the recipe is passed through a JSON object
# As such, INT parameters of the recipe are received in the get_recipe_config() dict as a Python float.
# If you absolutely require a Python int, use int(get_recipe_config()["my_int_param"])


#############################
# Your original recipe
#############################

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
ecommerce_transactions_with_ip_prepared = dataiku.Dataset("ecommerce_transactions_with_ip_prepared")
df = ecommerce_transactions_with_ip_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Filter to only US records
df_usa = df[df["MerchantIP_country"] == "United States"]

# Determine average purchase amount, per customer age and purchase hour
df_avg_purchase = df[["PurchaseHour", "CustomerAge", "OrderTotal"]].groupby(by=["PurchaseHour",
                                                                                "CustomerAge"], as_index=False).mean()

# Scatter plot of avg purchase amount, per customer age and purchase hour
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs = df_avg_purchase["PurchaseHour"]
ys = df_avg_purchase["CustomerAge"]
zs = df_avg_purchase["OrderTotal"]

ax.set_xlabel('Purchase Hour')
ax.set_ylabel('Customer Age')
ax.set_zlabel('Avg Order Total')
ax.set_title("US Transactions Only")

ax.scatter(xs, ys, zs)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Save scatter plot to folder
folder_for_plots = dataiku.Folder("MIrujfBg")
folder_path = folder_for_plots.get_path()

path_fig = os.path.join(folder_path, "US_transactions_scatter_plot")
plt.savefig(path_fig)
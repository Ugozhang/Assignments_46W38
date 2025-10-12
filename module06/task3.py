import os
import sys
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

# Get path of current .py file
script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)
# call the path of current .py 
os.chdir(script_dir)

df = pd.read_excel("Module 6 - Exercises Data.xlsx",sheet_name="Exercise 3",index_col=0)
TSR = df.index.values.astype(float)
pitch_angle = df.columns.values.astype(float)
power_coef = df.values

T_grid, p_grid = np.meshgrid(TSR, pitch_angle, indexing="ij")
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set_xlabel("Tip speed ratio")
ax.set_ylabel("pitch angle (degree)")
ax.set_zlabel("power coefficient")

ax.plot_surface(T_grid,p_grid,power_coef, cmap = "inferno", edgecolor ='none')

plt.show()


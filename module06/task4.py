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

# read data
df_Base = pd.read_excel("Module 6 - Exercises Data.xlsx",sheet_name="Exercise 4 - Baseline")
df_A = pd.read_excel("Module 6 - Exercises Data.xlsx",sheet_name="Exercise 4 - A")
df_B = pd.read_excel("Module 6 - Exercises Data.xlsx",sheet_name="Exercise 4 - B")

fig_scatter = plt.figure(figsize=(10,7),dpi=600)

ax = fig_scatter.subplots()
ax.set_xlabel("Time (s)")
ax.scatter(df_Base["Time (s)"],df_Base["Rotor speed (rpm)"],s=2)
ax.scatter(df_Base["Time (s)"],df_A["Rotor speed (rpm)"],s=2)
ax.scatter(df_Base["Time (s)"],df_B["Rotor speed (rpm)"],s=2)
plt.show()
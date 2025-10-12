import os
import sys
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

# 取得目前執行的 py 檔案所在路徑
script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)
# 切換目前工作目錄到該路徑
os.chdir(script_dir)

df = pd.read_excel("Module 6 - Exercises Data.xlsx",sheet_name="Exercise 2")

fig, ax1 = plt.subplots()
ax1.plot(df["Wind speed (m/s)"],df["Power (kW)"])
ax1.set_ylabel("Power (kW)")
ax1.set_xlabel("Wind speed (m/s)")

ax2 = ax1.twinx()
ax2.set_ylabel("Thrust (kN)")
ax2.plot(df["Wind speed (m/s)"],df["Thrust (kN)"])

ax3 = ax1.twinx()
ax3.set_ylabel("Rotor speed (rpm)")
ax3.plot(df["Wind speed (m/s)"],df["Rotor speed (rpm)"])

ax4 = ax1.twinx()
ax4.set_ylabel("Blade pitch (degrees)")
ax4.plot(df["Wind speed (m/s)"],df["Blade pitch (degrees)"])

plt.show()
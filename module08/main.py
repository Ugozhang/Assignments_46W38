import numpy as np
import matplotlib.pyplot as plt
import yaml
from pathlib import Path
from turbine_classes import WindTurbine, GeneralWindTurbine

# Make sure running under same folder each time by calling the path where main.py it is 
main_dir = Path(__file__).resolve().parent

# Assign files path
LEANWIND_wt_params_path = main_dir / "data" / "LEANWIND_Reference_8MW_164.yaml"
LEANWIND_wt_operation_curve_path = main_dir / "data" / "LEANWIND_Reference_8MW_164.csv"

# Read wt params
LEANWIND_wt_params = yaml.safe_load(LEANWIND_wt_params_path.read_text())
LEANWIND_wt_operation_curve = np.loadtxt(LEANWIND_wt_operation_curve_path, delimiter=',', skiprows=1)

# Build WindTurbine object
# LEANWIND params as General Turbine with cubic power curve
LEANWIND_wt_gen = GeneralWindTurbine(
    rotor_diameter=LEANWIND_wt_params["rotor_diameter"],
    hub_height=LEANWIND_wt_params["hub_height"],
    rated_power=LEANWIND_wt_params["rated_power"],
    v_in=LEANWIND_wt_params["cut_in_wind_speed"],
    v_rated=LEANWIND_wt_params["rated_wind_speed"],
    v_out=LEANWIND_wt_params["cut_out_wind_speed"],
    name=LEANWIND_wt_params["name"]
)
# LEANWIND params with experimental power curve
LEANWIND_wt_pc = WindTurbine(
    rotor_diameter=LEANWIND_wt_params["rotor_diameter"],
    hub_height=LEANWIND_wt_params["hub_height"],
    rated_power=LEANWIND_wt_params["rated_power"],
    v_in=LEANWIND_wt_params["cut_in_wind_speed"],
    v_rated=LEANWIND_wt_params["rated_wind_speed"],
    v_out=LEANWIND_wt_params["cut_out_wind_speed"],
    power_curve_data=LEANWIND_wt_operation_curve,
    name=LEANWIND_wt_params["name"]
)

# Create ws array for ploting
v_min = 0
v_max = LEANWIND_wt_params["cut_out_wind_speed"] + 1
v = np.linspace(v_min, v_max, 300)
P_general = LEANWIND_wt_gen.get_power(v)
P_pc = LEANWIND_wt_pc.get_power(v)

# Plot power curve
fig, ax1 = plt.subplots()
ax1.plot(v, P_general, label="General (cubic) model")
ax1.plot(v, P_pc, label="Tabulated power curve")
ax1.set_xlabel("Wind speed [m/s]")
ax1.set_ylabel("Power [kW]")
ax1.set_title("LEANWIND 8MW – Power curve comparison")
ax1.grid(True)
ax1.legend()
fig.tight_layout()
plt.show()

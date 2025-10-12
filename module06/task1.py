import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

energy_gen_source = {'Crude oil':0.377,
                     'Natural gas':0.204,
                     'Renewable Energy':0.195,
                     'Solid fuels':0.106,
                     'Nuclear Energy':0.118                     
                     }
energy_source = ['Crude oil','Natural gas','Renewable Energy','Solid fuels','Nuclear Energy']
share_in_percentage = [0.377,0.204,0.195,0.106,0.118]

plt.figure()
plt.pie(share_in_percentage,labels=energy_source,autopct="%1.1f%%")
plt.title("EU Energy Generation Shares (2023)")
plt.show()
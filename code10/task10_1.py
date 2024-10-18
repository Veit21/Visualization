import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataframe = pd.read_csv("co2_data.csv")

####################
# Task 1a          #
####################
fig, ax1 = plt.subplots()
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.ylim(0,500)











####################
# Task 1b          #
####################
ax2 = ax1.twinx()
plt.ylim(0,1)














# Show the result
plt.title('Total CO2 Emissions 1751-2017')
plt.tight_layout()
plt.show()
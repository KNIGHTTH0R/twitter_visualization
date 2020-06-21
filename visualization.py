import pickle 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import math 

# Update data files
#os.system('./pi_files/get_files.sh')

# Read data
data = pd.read_pickle('pi_files/volumes.pkl')
times = np.load('pi_files/times.npy')
print(data)
print(times)
print(len(times))
# Build plot and visualize data
# times = times[0:29]
for trend in data.iloc:
    if len(times) == len(trend.values) and trend.values[0] > 0:
        plt.plot(range(0,len(times)), trend.values, label='{}'.format(trend.name))
plt.legend(loc='upper left')
plt.xlabel('Time Steps (10min intervals)')
plt.ylabel('Tweet Volume')
# plt.axis([0, 29, 0, 500000])
plt.show()

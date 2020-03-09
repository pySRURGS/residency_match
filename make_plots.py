#
# After running `run_simulations.py`, this script is used to generate the plots 
#

import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from run_simulations import files, aliases
print(files)
plt.rcParams.update({'font.size': 8})
box_plot_data = []
for file in files:
    data = pd.read_csv(file)
    box_plot_data.append(data['match_rate'].values)
median_baseline = np.median(box_plot_data[0])
plt.figure(figsize=(8,3))
plt.hlines(median_baseline, 0.5, 6.5, colors='k', linestyles='dashed', label='')
plt.hlines(1, 0.5, 6.5, colors='k', linestyles='dashdot', label='')
medianprops = dict(linestyle='-', linewidth=2.5, color='k')
plt.boxplot(box_plot_data, labels=aliases, medianprops=medianprops)
plt.tight_layout()
plt.style.use('grayscale')
plt.savefig('figure.png')

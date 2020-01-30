import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from run_simulations import files
print(files)
plt.rcParams.update({'font.size': 8})
box_plot_data = []
for file in files:
    data = pd.read_csv(file)
    box_plot_data.append(data['match_rate'].values)
median_baseline = np.median(box_plot_data[0])
plt.figure(figsize=(4,3))
plt.hlines(median_baseline, 0.5, 5.5, colors='b', linestyles='dashed', label='')
plt.hlines(1, 0.5, 5.5, colors='k', linestyles='dashdot', label='')
medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')
plt.boxplot(box_plot_data, labels=['Baseline','Two\ninterviews\nper spot','Twenty\ninterviews\nper spot','Applicants\nchoose\nspecialty\nperfectly','Applicants\napply to 4\nspecialties'], medianprops=medianprops)
plt.tight_layout()
plt.show()
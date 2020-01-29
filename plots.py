import matplotlib.pyplot as plt
import pandas as pd 
files = ["10_2_0point2.csv", "2_2_0point2.csv", "20_2_0point2.csv", "10_2_10.csv","10_4_0point2.csv"]
box_plot_data = []
for file in files:
    data = pd.read_csv(file)
    box_plot_data.append(data['match_rate'].values)
plt.boxplot(box_plot_data, labels=['Baseline','Fewer\ninterviews\nper spot','More\ninterviews\nper spot','Applicants\nchoose\nspecialty\nperfectly','Applicants\napply\nto many\nspecialties'])
plt.tight_layout()
plt.show()
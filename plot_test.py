import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('crop_csv_file.xlsx')

x="Crop_Year"
y="Production"
plot=sns.lineplot(data[x],data[y])
plot.figure.savefig("myfig.png")
plt.show()
#sns.barplot(data["Season"],data["Production"])

#ln1

import numpy as np
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns  # visualization tool
import csv


#ln2
dataPath = pd.read_csv('C:/Users/steph/Desktop/countrydata.txt')
dataPath.info()


#ln3 basic data correlation
dataPath.corr()

#regional GDP, literacy and agriculture NEEDS WORK
dataPath.groupby('Region')[['GDP ($ per capita)', 'Literacy (%)', 'Agriculture']].median()



#ln4 cool heatmap
f,ax = plt.subplots(figsize=(18, 18))
sns.heatmap(dataPath.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()

dataPath.describe()

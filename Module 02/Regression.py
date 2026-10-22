import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
Data preparation
'''
df = pd.read_csv('data.csv')

#Make every column name lowercase and connected by underscores
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')

#Same with the values
strings = list(df.dtypes[df.dtypes == 'str'].index)

for col in strings:
    df[col] = df[col].str.lower().str.replace(' ', '_')

print(df.head())

'''
EDA
'''
for col in df.columns:
    print(col)
    print(df[col].unique()[:5])
    print(df[col].nunique() )
    print()

#Distribution of prices
sns.histplot(df.msrp[df.msrp < 100000], bins = 50)
plt.show()
#Long-tailed distribution -> not ideal for ML

#Logarithmic transformation
np.log([0 + 1, 1 + 1, 10 + 1, 100 + 1, 1000 + 1])
#Numpy has an integrated function
np.log1p([0,1,10,100,1000])

price_logs = np.log1p(df.msrp)
print(price_logs)

sns.histplot(price_logs, bins = 50)
plt.show()
#Now it resembles a normal distribution


#We will need to consider the missing (NaN) values
print(df.isnull().sum())



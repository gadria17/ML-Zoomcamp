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




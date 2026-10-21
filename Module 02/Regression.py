import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')

#Make every column name lowercase and connected by underscores
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')

#Same with the values
strings = list(df.dtypes[df.dtypes == 'str'].index)

for col in strings:
    df[col] = df[col].str.lower().str.replace(' ', '_')

print(df.head())


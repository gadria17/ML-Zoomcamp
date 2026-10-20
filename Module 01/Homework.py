import numpy as np
import pandas as pd

pandas_version = pd.__version__
print(pandas_version)

#Q1: Pandas version = 3.0.6


df = pd.read_csv('car_fuel_efficiency_2026.csv')
print('Q2')
print(df)

#Q2: We can see there are 10000 rows=records in the datasheet

print('Q3')
print(df.fuel_type.unique())

#Q3: ['Gasoline', 'Diesel', 'Hybrid'] = 3
print('Q4')
print(df.isnull().sum())

#Q4: Horsepower and acceleration columns have null values = 2 columns

print('Q5')
max_asia = df.groupby('origin').fuel_efficiency_mpg.max().iloc[0]
print(max_asia)

#Q5: The max value of fuel efficiency in Asia is 41.1

print('Q6')
mdhp = df['horsepower'].median()
mohp = df['horsepower'].mode()
df2 = df.fillna(df['horsepower'])
print('Original horsepower median:' + str(mdhp))
print(mohp)
print('Modified horsepower median: ' +  str(df2['horsepower'].median()))

#Q6: The median value of the horsepower hasn't changed

#Select the asian cars
asian = df[df['origin'] == 'Asia']
#Select only the columns vehicle_weight and model_year
asian = asian[['vehicle_weight', 'model_year']]
#First 7 values
asian = asian.head(7)
#Get the underlying array
X = asian.values
print(X.shape)
#Matrix-matrix multiplication + inverse
XTX = X.T @ X
XTX = np.linalg.inv(XTX)
#We define y and compute w
y = np.array([1100, 1300, 800, 900, 1000, 1100, 1200])
print(y.shape)
result = XTX @ X.T
w = result @ y
sum = w.sum()
print(sum.round(4))

#Q7: The result is approximately 0.3692










import numpy as np
import pandas as pd

#First way of creating a DataFrame: list of lists of data + column index (another list)
data = [
    ['Nissan', 'Stanza', 1991, 138, 4, 'MANUAL', 'sedan', 2000],
    ['Hyundai', 'Sonata', 2017, None, 4, 'AUTOMATIC', 'Sedan', 27150],
    ['Lotus', 'Elise', 2010, 218, 4, 'MANUAL', 'convertible', 54990],
    ['GMC', 'Acadia',  2017, 194, 4, 'AUTOMATIC', '4dr SUV', 34450],
    ['Nissan', 'Frontier', 2017, 261, 6, 'MANUAL', 'Pickup', 32340],
]

columns = [
    'Make', 'Model', 'Year', 'Engine HP', 'Engine Cylinders',
    'Transmission Type', 'Vehicle_Style', 'MSRP'
]

df = pd.DataFrame(data, columns=columns)
print(df)

#Second way: dictionaries
data2 = [
    {
        "Make": "Nissan",
        "Model": "Stanza",
        "Year": 1991,
        "Engine HP": 138.0,
        "Engine Cylinders": 4,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "sedan",
        "MSRP": 2000
    },
    {
        "Make": "Hyundai",
        "Model": "Sonata",
        "Year": 2017,
        "Engine HP": None,
        "Engine Cylinders": 4,
        "Transmission Type": "AUTOMATIC",
        "Vehicle_Style": "Sedan",
        "MSRP": 27150
    },
    {
        "Make": "Lotus",
        "Model": "Elise",
        "Year": 2010,
        "Engine HP": 218.0,
        "Engine Cylinders": 4,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "convertible",
        "MSRP": 54990
    },
    {
        "Make": "GMC",
        "Model": "Acadia",
        "Year": 2017,
        "Engine HP": 194.0,
        "Engine Cylinders": 4,
        "Transmission Type": "AUTOMATIC",
        "Vehicle_Style": "4dr SUV",
        "MSRP": 34450
    },
    {
        "Make": "Nissan",
        "Model": "Frontier",
        "Year": 2017,
        "Engine HP": 261.0,
        "Engine Cylinders": 6,
        "Transmission Type": "MANUAL",
        "Vehicle_Style": "Pickup",
        "MSRP": 32340
    }
]

df2 = pd.DataFrame(data2)

print(df2)

#Selects the nth first rows
print(df.head(n=2))

print(df.Make)
companies = df['Make']

years = df.Year

print(companies)
print(years)

#Select columns
var1 = df[['Make','Transmission Type']]

#Add a new  column and modify it
df['id'] = ['29492','23913','01843','12931','2283']

print(df)

df['id'] = ['0','23913','01843','12931','2283']

print(df)

#Eliminate a column
del df['id']
print(df)


#Obtain and modify row index
df.index = ['a','b','c','d','e']
print(df)

#Obtain a column by its index (loc and iloc)
print(df.loc['a'])
print(df.iloc[0])

#Reset the index without altering the original DataFrame
print(df.reset_index(drop=True))
print(df)

#Element-wise operations
print(df.Year - 2000)

print(df['Year'] <= 2000)

#Filtering DataFrames
print(df[df['Year'] <= 2000])


#Operation on the String (.str)
df['Vehicle_Style'] = df['Vehicle_Style'].str.title()
print(df['Vehicle_Style'])

print( df.MSRP.min())

print( df.describe().round(2))

#Unique values in the DataFrame
print(df.nunique())

print(df.isnull())

#SQL equivalent to grouping

print(df.groupby('Transmission Type').MSRP.mean())

#NumPy arrays
print(df.MSRP.values)

#Restores the original dictionary that was used to create the DataFrame
df.to_dict(orient='records')


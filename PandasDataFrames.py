#Pandas DataFrames

#Create a simple Pandas DataFrame:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

#refer to the row index:
print(df.loc[0])

#Return row 0 and 1:

#use a list of indexes:
print(df.loc[[0, 1]])

#Add a list of names to give each row a name:


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

#Return "day2":

#refer to the named index:
print(df.loc["day2"])

#Load a comma separated file (CSV file) into a DataFrame:


df = pd.read_csv('data.csv')

print(df)
# Numpy Shape Attribute
import pandas as pd

df = pd.read_csv("titanic.csv")
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr.shape)

# This result means we have 887 rows and 3 columns.
'''
Use the shape attribute to find the number of rows and number columns for a Numpy array. 
You can also use the shape attribute on a pandas DataFrame (df.shape).
'''

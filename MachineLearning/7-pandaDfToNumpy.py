# Converting from a Pandas DataFrame to a Numpy Array
import pandas as pd

df = pd.read_csv("titanic.csv")
print(df[['Pclass', 'Fare', 'Age']].values)

'''
The values attribute of a Pandas DataFrame give the data as a 2d numpy array.
'''

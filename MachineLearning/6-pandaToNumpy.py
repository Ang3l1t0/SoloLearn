import pandas as pd

df = pd.read_csv("titanic.csv")
print(df["Fare"].values)

'''
The values attribute of a Pandas Series give the data as a numpy array.
'''

import pandas as pd

df = pd.read_csv("titanic.csv")
small_df = df[['Age', 'Sex', 'Survived']]
print(small_df.head())

'''
When selecting a single column from a Pandas DataFrame, 
we use single square brackets. When selecting multiple columns, 
we use double square brackets.
'''

import pandas as pd

df = pd.read_csv("titanic.csv")
small_df = df[['Age', 'Sex', 'Survived']]
print(small_df.head())

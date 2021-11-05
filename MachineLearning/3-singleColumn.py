import pandas as pd

df = pd.read_csv("titanic.csv")
col = df['Fare']
print(col)

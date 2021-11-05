import pandas as pd

df = pd.read_csv("titanic.csv")
df['male'] = df['Sex'] == 'male'
print(df.head())

'''
Often our data isn’t in the ideal format. 
Luckily Pandas makes it easy for us to create 
new columns based on our data so we can format it appropriately.
'''

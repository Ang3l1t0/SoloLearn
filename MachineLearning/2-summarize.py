import pandas as pd

pd.options.display.max_columns = 6
df = pd.read_csv('titanic.csv')
print(df.describe())

'''
We use the Pandas describe method to start building some intuition about our data.


Let's review what each of these statistics means:
Count: This is the number of rows that have a value. In our case, every passenger has a value for each of the columns, so the value is 887 (the total number of passengers).
Mean: Recall that the mean is the standard average.
Std: This is short for standard deviation. This is a measure of how dispersed the data is.
Min: The smallest value
25%: The 25th percentile
50%: The 50th percentile, also known as the median.
75%: The 75th percentile
Max: The largest value
'''
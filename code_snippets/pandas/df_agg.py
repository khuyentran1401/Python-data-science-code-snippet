import pandas as pd 

df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [2, 3, 4, 5]})

print(df.agg({'a': ['sum', 'mean'], 'b': ['min', 'max']}))

"""
         a    b
sum   10.0  NaN
mean   2.5  NaN
min    NaN  2.0
max    NaN  5.0
"""

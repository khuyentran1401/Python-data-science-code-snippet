import pandas as pd 

df = pd.DataFrame({'a': [1, 3, 7, 11, 14, 17]})

bins = [0, 5, 10, 15, 20]
df['binned'] = pd.cut(df['a'], bins=bins)

print(df)
"""
    a    binned
0   1    (0, 5]
1   3    (0, 5]
2   7   (5, 10]
3  11  (10, 15]
4  14  (10, 15]
5  17  (15, 20]
"""
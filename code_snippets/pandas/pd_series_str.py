import pandas as pd

fruits = pd.Series(['Orange', 'Apple', 'Grape'])
print(fruits)
"""
0    Orange
1     Apple
2     Grape
dtype: object
"""

print(fruits.str.lower())
"""
0    orange
1     apple
2     grape
dtype: object
"""

print(fruits.str.lower().str.replace("e", "a"))
"""
0    oranga
1     appla
2     grapa
dtype: object
"""


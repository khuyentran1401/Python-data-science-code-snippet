import pandas as pd 

df1 = pd.DataFrame({'left_key': [1, 2, 3], 'a': [4, 5, 6]})
df2 = pd.DataFrame({'right_key': [1, 2, 3], 'a': [5, 6, 7]})
print(df1.merge(df2, left_on='left_key', right_on='right_key'))
""" 
   left_key  a_x  right_key  a_y
0         1    4          1    5
1         2    5          2    6
2         3    6          3    7
"""

print(df1.merge(df2, left_on='left_key', right_on='right_key',
        suffixes=('_left', '_right')))
""" 
   left_key  a_left  right_key  a_right
0         1       4          1        5
1         2       5          2        6
2         3       6          3        7
"""

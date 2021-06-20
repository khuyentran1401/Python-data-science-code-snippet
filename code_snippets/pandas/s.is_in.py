import pandas as pd 

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df)
""" 
   a  b
0  1  4
1  2  5
2  3  6
"""

l = [1, 2, 6, 7]
print(df.a.isin(l))
""" 
0     True
1     True
2    False
Name: a, dtype: bool
"""

df = df[df.a.isin(l)]
print(df)
""" 
   a  b
0  1  4
1  2  5
"""
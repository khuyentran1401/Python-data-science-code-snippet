import pandas as pd 

s = pd.Series([5, 2, 15, 13, 6, 10])

print(s[s.between(0, 10)])
""" 
0     5
1     2
4     6
5    10
dtype: int64
"""
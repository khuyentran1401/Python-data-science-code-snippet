import pandas as pd 

df = pd.DataFrame({'a': [20, 35, 10], 'b': [1, 2, 3]})
print(df)
"""
    a  b
0  20  1
1  35  2
2  10  3
"""

print(df.a.pct_change())
""" 
0         NaN
1    0.750000
2   -0.714286
Name: a, dtype: float64
"""
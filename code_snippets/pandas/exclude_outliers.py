import pandas as pd

data = {"col0": [9, -3, 0, -1, 5]}
df = pd.DataFrame(data)

lower = df.col0.quantile(0.05)
upper = df.col0.quantile(0.95)

print(df.clip(lower=lower, upper=upper))
""" 
   col0
0   8.2
1  -2.6
2   0.0
3  -1.0
4   5.0
"""

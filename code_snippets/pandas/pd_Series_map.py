import pandas as pd

s = pd.Series(["a", "b", "c"])

print(s.map({"a": 1, "b": 2, "c": 3}))
"""
0    1
1    2
2    3
dtype: int64
"""

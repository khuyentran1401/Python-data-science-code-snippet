import pandas as pd

df = pd.DataFrame({"col1": ["a", "a", "b", "c", "c", "d"], "col2": [4, 5, 6, 7, 8, 9]})
print(df.groupby("col1").sample(n=1))

"""
  col1  col2
0    a     4
2    b     6
4    c     8
5    d     9
"""

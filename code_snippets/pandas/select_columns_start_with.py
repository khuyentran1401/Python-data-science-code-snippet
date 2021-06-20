import pandas as pd

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [3, 4, 5], "year": [2019, 2019, 2020]})

chosen_cols = df.columns.str.startswith('col')
print(chosen_cols)
"""[ True  True False]"""

print(df.loc[:, chosen_cols])
""" 
   col1  col2
0     1     3
1     2     4
2     3     5
"""

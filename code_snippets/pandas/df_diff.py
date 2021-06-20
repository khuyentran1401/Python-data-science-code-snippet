import pandas as pd 
df = pd.DataFrame({'a': [1, 2, 3, 4], 'b': [2, 3, 4, 6]})
diff = df.diff()
print(diff)
""" 
     a    b
0  NaN  NaN
1  1.0  1.0
2  1.0  1.0
3  1.0  2.0
"""

shift = diff.shift(-1)
print(shift)
""" 
     a    b
0  1.0  1.0
1  1.0  1.0
2  1.0  2.0
3  NaN  NaN
"""

processed_df = shift.dropna()
print(processed_df)
""" 
     a    b
0  1.0  1.0
1  1.0  1.0
2  1.0  2.0
"""
import numpy as np
import pandas as pd

df = pd.DataFrame({"a": [1, np.nan, 3], "b": [4, 5, np.nan], "c": [1, 2, 3]})
print(df)
"""
     a    b  c
0  1.0  4.0  1
1  NaN  5.0  2
2  3.0  NaN  3
"""

df = df.fillna(method="ffill")
print(df)
"""
     a    b  c
0  1.0  4.0  1
1  1.0  5.0  2
2  3.0  5.0  3
"""

import pandas as pd 

df = pd.DataFrame({'col1': ['a', 'b', 'c'], 'col2': [1, 2, 3],
                    'col3': [0.1, 0.2, 0.3]})

print(df.info())
""" 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   col1    3 non-null      object 
 1   col2    3 non-null      int64  
 2   col3    3 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 200.0+ bytes
"""

print(df.select_dtypes(include=['int64', 'float64']))
""" 
   col2  col3
0     1   0.1
1     2   0.2
2     3   0.3
""" 

print(df.select_dtypes(exclude=['object']))
"""
   col2  col3
0     1   0.1
1     2   0.2
2     3   0.3
"""
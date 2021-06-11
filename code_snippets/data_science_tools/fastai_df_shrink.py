# pip install fastai

from fastai.tabular.core import df_shrink
import pandas as pd 

df = pd.DataFrame({"col1": [1, 2, 3], "col2": [1.0, 2.0, 3.0]})
print(df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   col1    3 non-null      int64  
 1   col2    3 non-null      float64
dtypes: float64(1), int64(1)
memory usage: 176.0 bytes
""" 

new_df = df_shrink(df)
print(new_df.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   col1    3 non-null      int8   
 1   col2    3 non-null      float32
dtypes: float32(1), int8(1)
memory usage: 143.0 bytes
"""
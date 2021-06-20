import pandas as pd 

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})

df = (df.assign(col3=lambda x: x.col1 * 100 + x.col2)
    .assign(col4=lambda x: x.col2 * x.col3)
    )
print(df)
""" 
   col1  col2  col3  col4
0     1     3   103   309
1     2     4   204   816
"""
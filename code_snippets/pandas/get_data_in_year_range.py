import pandas as pd 
from datetime import datetime 
df = pd.DataFrame({'date': [datetime(2018, 10, 1),
                            datetime(2019, 10, 1),
                            datetime(2020, 10, 1)],
                    'val': [1, 2, 3]}).set_index('date')

print(df)
""" 
            val
date           
2018-10-01    1
2019-10-01    2
2020-10-01    3
"""
print(df.loc['2019':])
""" 
            val
date           
2019-10-01    2
2020-10-01    3
"""
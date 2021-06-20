import pandas as pd
from datetime import date

df = pd.DataFrame({'date': [date(2021, 1, 20), date(2021, 1, 21), date(2021, 1, 22),
                            date(2021, 1, 23), date(2021, 1, 24)],
                    'value': [1, 2, 3, 4, 5]}).set_index('date')

print(df)
""" 
            value
date             
2021-01-20      1
2021-01-21      2
2021-01-22      3
2021-01-23      4
2021-01-24      5
"""

print(df.rolling(3).mean())
""" 
            value
date             
2021-01-20    NaN
2021-01-21    NaN
2021-01-22    2.0
2021-01-23    3.0
2021-01-24    4.0
"""

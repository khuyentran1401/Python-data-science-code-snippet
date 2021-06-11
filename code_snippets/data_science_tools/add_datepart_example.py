import pandas as pd 
from fastai.tabular.core import add_datepart
from datetime import datetime

df = pd.DataFrame({'date': [datetime(2020, 2, 5), datetime(2020, 2, 6),
                            datetime(2020, 2, 7), datetime(2020, 2, 8)],
                'val': [1, 2, 3, 4]})

df = add_datepart(df, 'date')
print(df.columns)                
""" 
Index(['val', 'Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
       'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start',
       'Is_year_end', 'Is_year_start', 'Elapsed'],
      dtype='object')
"""
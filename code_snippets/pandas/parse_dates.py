import pandas as pd 

df = pd.read_csv('data1.csv', parse_dates=['date_column_1', 'date_column_2'])
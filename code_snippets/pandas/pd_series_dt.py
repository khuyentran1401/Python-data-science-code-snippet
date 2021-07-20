import pandas as pd

df = pd.DataFrame({'date': ['2021/05/13 15:00', '2022-6-20 14:00'],
		   'values': [1, 3]})

df['date'] = pd.to_datetime(df['date'])

print(df['date'].dt.year)

print(df['date'].dt.time)


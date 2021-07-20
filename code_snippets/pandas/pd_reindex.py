import pandas as pd 

s = pd.Series([1, 2, 3], index=['2021-07-20', '2021-07-23', '2021-07-25'])
s.index = pd.to_datetime(s.index)
print(s)

# Get dates ranging from 2021/7/20 to 2021/7/25
new_index = pd.date_range('2021-07-20', '2021-07-25')

# Conform Series to new index
new_s = s.reindex(new_index, fill_value=0)
print(new_s)
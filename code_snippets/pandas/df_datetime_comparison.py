import pandas as pd

df = pd.DataFrame(
    {"date": pd.date_range(start="2021-7-19", end="2021-7-23"), "value": list(range(5))}
)
print(df)
"""
        date  value
0 2021-07-19      0
1 2021-07-20      1
2 2021-07-21      2
3 2021-07-22      3
4 2021-07-23      4
"""

filtered_df = df[df.date <= "2021-07-21"]
print(filtered_df)
"""
        date  value
0 2021-07-19      0
1 2021-07-20      1
2 2021-07-21      2
"""

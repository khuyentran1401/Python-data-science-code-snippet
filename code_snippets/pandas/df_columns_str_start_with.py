import pandas as pd

df = pd.DataFrame({'pricel': [1, 2, 3],
                    'price2': [2, 3, 4],
                    'year': [2020, 2021, 2021]})

mask = df.columns.str.startswith('price')
print(df.loc[:, mask])

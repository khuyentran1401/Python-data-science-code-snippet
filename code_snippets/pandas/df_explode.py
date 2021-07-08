import pandas as pd 

df = pd.DataFrame({'a': [[1, 2], [4, 5]], 'b': [11, 13]})
print(df)

print(df.explode('a'))
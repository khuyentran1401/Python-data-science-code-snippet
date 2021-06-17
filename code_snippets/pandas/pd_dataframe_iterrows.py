import pandas as pd 

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
for idx, row in df.iterrows():
    print(f"a: {row['a']}, b: {row['b']}")
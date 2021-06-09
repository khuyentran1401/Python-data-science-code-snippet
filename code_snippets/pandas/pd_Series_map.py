import pandas as pd

s = pd.Series(['a', 'b', 'c'])

print(s.map({'a': 1, 'b': 2, 'c': 3}))
import pandas as pd 

df = pd.DataFrame({'col1': ['large', 'small', 'mini', 'medium', 'mini'],
                'col2': [1, 2, 3, 4, 5]})
ordered_sizes = 'large', 'medium', 'small', 'mini'

df.col1 = df.col1.astype('category')
df.col1.cat.set_categories(ordered_sizes, ordered=True, inplace=True)
print(df.sort_values(by='col1'))
""" 
     col1  col2
0   large     1
3  medium     4
1   small     2
2    mini     3
4    mini     5
"""
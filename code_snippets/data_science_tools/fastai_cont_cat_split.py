import pandas as pd
from fastai.tabular.core import cont_cat_split

df = pd.DataFrame(
    {
        "col1": [1, 2, 3, 4, 5],
        "col2": ["a", "b", "c", "d", "e"],
        "col3": [1.0, 2.0, 3.0, 4.0, 5.0],
    }
)

cont_names, cat_names = cont_cat_split(df)
print(cont_names) # ['col3']
print(cat_names) # ['col1', 'col2']

cont_names, cat_names = cont_cat_split(df, max_card=3)
print(cont_names) # ['col1', 'col3']
print(cat_names) # ['col2']

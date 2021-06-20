import pandas as pd 
from tqdm import tqdm 
import time 

df = pd.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [2, 3, 4, 5, 6]})

tqdm.pandas()
def func(row):
    time.sleep(1)
    return row + 1

df['a'].progress_apply(func)
"""
80%|██████████████████████████▍      | 4/5 [00:03<00:00,  1.22it/s]
"""
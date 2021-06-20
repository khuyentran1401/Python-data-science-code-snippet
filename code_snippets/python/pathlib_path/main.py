from pathlib import Path 
import pandas as pd

DATA_DIR = Path('data', 'processed')

df1 = pd.read_csv(DATA_DIR / 'data1.csv')
df2 = pd.read_csv(DATA_DIR / 'data2.csv')
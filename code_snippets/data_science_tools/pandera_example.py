# pip install pandera 

import pandera as pa
from pandera import check_input
import pandas as pd

df = pd.DataFrame({'col1': [5.0, 8.0, 10.0],
					'col2': ['text_1', 'text_2', 'text_3']})
schema = pa.DataFrameSchema({
		 "col1": pa.Column(float, pa.Check(lambda minute: 5 <= minute)),
		 "col2": pa.Column(str, pa.Check.str_startswith("text_"))
})
validated_df = schema(df)
print(validated_df)
"""
   col1    col2
0   5.0  text_1
1   8.0  text_2
2  10.0  text_3
"""

@check_input(schema)
def plus_three(df):
	df['col1_plus_3'] = df['col1'] + 3
	return df 

print(plus_three(df))
""" 
   col1    col2  col1_plus_3
0   5.0  text_1          8.0
1   8.0  text_2         11.0
2  10.0  text_3         13.0
"""
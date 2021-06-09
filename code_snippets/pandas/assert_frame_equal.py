from pandas.testing import assert_frame_equal
import pandas as pd 


df1 = pd.DataFrame({'coll': [1,2,3], 'col2': [4,5,6]})
df2 = pd.DataFrame({'coll': [1,3,4], 'col2': [4,5,6]})
assert_frame_equal(df1, df2)

"""
AssertionError: DataFrame.iloc[:, 0] (column name="coll") are different

DataFrame.iloc[:, 0] (column name="coll") values are different (66.66667 %)
[index]: [0, 1, 2]
[left]:  [1, 2, 3]
[right]: [1, 3, 4]
"""



from sklearn.datasets import load_iris
import pandas as pd 

X, y = load_iris(as_frame=True, return_X_y=True)
df = pd.concat([X, pd.DataFrame(y, columns=['target'])], axis=1)
print(df.memory_usage())
""" 
Index                 128
sepal length (cm)    1200
sepal width (cm)     1200
petal length (cm)    1200
petal width (cm)     1200
target               1200
dtype: int64
""" 
df['target'] = df['target'].astype('category')
print(df.memory_usage())
""" 
Index                 128
sepal length (cm)    1200
sepal width (cm)     1200
petal length (cm)    1200
petal width (cm)     1200
target                282
dtype: int64
"""

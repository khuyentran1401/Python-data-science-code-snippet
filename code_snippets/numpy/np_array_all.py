import numpy as np 

a = np.array([[1, 2, 1], [2, 2, 5]])
print(a)

# Find if all elements are less than 3 in each column
print((a < 3).all(axis=0))

# Find if all elements are less than 3 in each row
print((a < 3).all(axis=1))

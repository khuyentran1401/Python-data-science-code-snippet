import numpy as np

arr = np.array([[1, 4, 10, 15], [2, 3, 8, 9]])

# Multiply values that are less than 5 by 2
print(np.where(arr < 5, arr * 2, arr))
"""
[[ 2  8 10 15]
 [ 4  6  8  9]]
"""

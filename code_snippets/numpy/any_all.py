import numpy as np

a = np.array([[1, 2, 1], [2, 2, 5]])

# get the rows whose all values are fewer than 3
mask_all = (a<3).all(axis=1)
print(a[mask_all])
"""
[[1 2 1]]
"""

mask_any = (a<3).any(axis=1)
print(a[mask_any])
""" 
[[1 2 1]
 [2 2 5]]
"""
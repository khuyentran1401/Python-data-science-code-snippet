import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 1, 2])

print(a < 2)
"""
[ True False False]
"""

print(a < b)
"""
[ True False False]
"""

print(a[a < b])
"""
[1]
"""
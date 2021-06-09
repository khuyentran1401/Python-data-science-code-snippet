import numpy as np
arr = np.array([[1, 2], [3, 41]])
print(arr)

print(np.ravel(arr))

print(np.ravel(arr, order="F"))
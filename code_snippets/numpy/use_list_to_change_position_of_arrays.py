import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Old array\n", arr)

new_row_position = [1, 2, 0]
new_arr = arr[new_row_position, : ]
print("New array\n", new_arr)

arr = ['a', 'b', 'c', 'd', 'e']

# Instead of this
for i in range(len(arr)):
    print(i, arr[i])
""" 
0 a
1 b
2 c
3 d
4 e
"""

# Use this
for i, val in enumerate(arr):
    print(i, val)
""" 
0 a
1 b
2 c
3 d
4 e
"""
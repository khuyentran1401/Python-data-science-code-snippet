arr = {'a': [1, 2], 'b': 1}
for key, val in arr.items():
    try:
        print(val[0])
    except Exception as e:
        print(e)
""" 
1
'int' object is not subscriptable
"""
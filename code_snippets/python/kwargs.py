parameters = {'a': 1, 'b': 2}
def example(c, **kwargs):
    print(kwargs)
    for val in kwargs.values():
        print(c + val)

example(c=3, **parameters)
""" 
{'a': 1, 'b': 2}
4
5
"""
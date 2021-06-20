def return_many_values():
    a = 1
    b = 2
    c = 3 
    d = 4
    # Instead of return a, b, c, d
    return {'a': a, 'b': b, 'c': c, 'd': d}

values = return_many_values()
print(values['a'])
# 1
print(values['b'])
# 2
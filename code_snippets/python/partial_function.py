from functools import partial


def linear_func(x, a, b):
    return a * x + b


linear_func_partial = partial(linear_func, a=2, b=3)
print(linear_func_partial(2))
print(linear_func_partial(4))

from timeit import timeit
from numpy.random import randint

def built_in_sum(l: list):
    return sum(l)

def custom_sum(l: list):
    sum_val = 0
    for num in l:
        sum_val += num 
    return sum_val

l = randint(0, 100, size=100_000)
expSize = 100

built_in_time = timeit("built_in_sum(l)", number=expSize, globals=globals())
custom_time = timeit("custom_sum(l)", number=expSize, globals=globals())
print(custom_time/built_in_time)
# 1.2499071011706575
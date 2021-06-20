import time 
import timeit 

def func():
    """comprehension"""
    l = [i for i in range(10_000)]

def func2():
    """list range"""
    l = list(range(10_000))

expSize = 1000
time1 = timeit.timeit(func, number=expSize)
time2 = timeit.timeit(func2, number=expSize)

print(time1/time2)
# 1.738841810509789
import heapq
import random
from timeit import timeit

random.seed(0)
l = random.sample(range(0, 10000), 10000)

def get_n_max_sorting(l: list, n: int):
    l = sorted(l, reverse=True)
    return l[:n]

def get_n_max_heapq(l: list, n: int):
    return heapq.nlargest(n, l)

expSize = 1000
n = 100
time_sorting = timeit("get_n_max_sorting(l, n)", number=expSize,
                        globals=globals())
time_heapq = timeit('get_n_max_heapq(l, n)', number=expSize,
                    globals=globals())

ratio = round(time_sorting/time_heapq, 3)
print(f'Run {expSize} experiments. Using heapq is {ratio} times'
'faster than using sorting')
""" 
Run 1000 experiments. Using heapq is 2.659 timesfaster than using sorting
"""
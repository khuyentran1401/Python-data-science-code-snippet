from timeit import timeit

def for_loop():
    result = []
    for i in range(1_000_000):
        result.append(i)
    return result

def list_comprehesion():
    return [i for i in range(1_000_000)]

expSize = 1000
time1 = timeit(for_loop, number=expSize)
time2 = timeit(list_comprehesion, number=expSize)

print(time1/time2)
# 1.4560360180596434


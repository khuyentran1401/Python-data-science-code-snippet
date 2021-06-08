python -m timeit "arr = []
for i in range(100):
    arr.append(i)"

python -m timeit "arr = [i for i in range(100)]"

python -m timeit "arr = list(range(100))"


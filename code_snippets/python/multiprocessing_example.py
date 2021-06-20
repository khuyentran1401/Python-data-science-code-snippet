from joblib import Parallel, delayed
import multiprocessing

def add_three(num: int):
    return num + 3

num_cores = multiprocessing.cpu_count()
results = Parallel(n_jobs=num_cores)(delayed(add_three)(i) for i in range(10))
print(results)
# [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
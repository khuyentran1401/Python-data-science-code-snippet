# pip install swifter
from time import time
from sklearn.datasets import fetch_california_housing
from scipy.special import boxcox1p
import swifter
import timeit

X, y = fetch_california_housing(return_X_y=True, as_frame=True)

def pandas_apply():
    X["AveRooms"].apply(lambda x: boxcox1p(x, 0.25))


def swifter_apply():
    X["AveRooms"].swifter.apply(lambda x: boxcox1p(x, 0.25))

num_experiments = 100
pandas_time = timeit.timeit(pandas_apply, number=num_experiments)
swifter_time = timeit.timeit(swifter_apply, number=num_experiments)

pandas_vs_swifter = round(pandas_time/swifter_time, 2)
print(f'Swifter apply is {pandas_vs_swifter} times faster than Pandas apply')
# Swifter apply is 12.54 times faster than Pandas apply
import numpy as np
from numpy.testing import assert_almost_equal, assert_array_equal

a = np.array([[1.222, 2.222], [3.222, 4.222]])
test = np.array([[1.221, 2.221], [3.221, 4.221]])
assert_almost_equal(a, test, decimal=2)

assert_array_equal(a, test)
"""AssertionError: 
Arrays are not equal

Mismatched elements: 4 / 4 (100%)
Max absolute difference: 0.001
Max relative difference: 0.000819
"""

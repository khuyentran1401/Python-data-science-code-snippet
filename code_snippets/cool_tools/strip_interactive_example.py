
from strip_interactive import run_interactive

code = """
>>> import numpy as np
>>> print(np.array([1,2,3]))
[1 2 3]
>>> print(np.array([4,5,6]))
[4 5 6]
"""

run_interactive(code)


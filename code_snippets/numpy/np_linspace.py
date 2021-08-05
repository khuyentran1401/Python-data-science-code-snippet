import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2, 4, num=10)
print(x)
"""
[2.         2.22222222 2.44444444 2.66666667 2.88888889 3.11111111
 3.33333333 3.55555556 3.77777778 4.        ]
"""

y = np.arange(10)

plt.plot(x, y)
plt.show()

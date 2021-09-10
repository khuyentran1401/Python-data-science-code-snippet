import numpy as np
from distfit import distfit

X = np.random.normal(0, 3, 1000)

# Initialize model
dist = distfit()

# Find best theoretical distribution for empirical data X
distribution = dist.fit_transform(X)
dist.plot()

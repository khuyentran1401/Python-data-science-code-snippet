# pip install pycausalimpact

import numpy as np
import pandas as pd 
from statsmodels.tsa.arima_process import ArmaProcess
from causalimpact import CausalImpact

# Generate random sample

np.random.seed(0)
ar = np.r_[1, 0.9]
ma = np.array([1])
arma_process = ArmaProcess(ar, ma)

X = 50 + arma_process.generate_sample(nsample=1000)
y = 1.6 * X + np.random.normal(size=1000)

# There is a change starting from index 800
y[800:] += 10

data = pd.DataFrame({'y': y, 'X': X}, columns=['y', 'X'])
pre_period = [0, 799]
post_period = [800, 999]

ci = CausalImpact(data, pre_period, post_period)
print(ci.summary())
print(ci.summary(output='report'))
ci.plot()
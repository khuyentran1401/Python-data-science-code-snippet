from itertools import product

params = {
    "learning_rate": [1e-1, 1e-2, 1e-3],
    "batch_size": [16, 32, 64],
}

for vals in product(*params.values()):
    combination = dict(zip(params.keys(), vals))
    print(combination)
"""
{'learning_rate': 0.1, 'batch_size': 16}
{'learning_rate': 0.1, 'batch_size': 32}
{'learning_rate': 0.1, 'batch_size': 64}
{'learning_rate': 0.01, 'batch_size': 16}
{'learning_rate': 0.01, 'batch_size': 32}
{'learning_rate': 0.01, 'batch_size': 64}
{'learning_rate': 0.001, 'batch_size': 16}
{'learning_rate': 0.001, 'batch_size': 32}
{'learning_rate': 0.001, 'batch_size': 64}
"""

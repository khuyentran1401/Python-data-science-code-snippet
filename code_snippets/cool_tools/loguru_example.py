from sklearn.metrics import mean_squared_error
import numpy as np
from loguru import logger

logger.add("file_{time}.log", format="{time} {level} {message}")

@logger.catch
def evaluate_result(y_true: np.array, y_pred: np.array):
    mean_square_err = mean_squared_error(y_true, y_pred)
    root_mean_square_err = mean_square_err ** 0.5

y_true = np.array([1, 2, 3])
y_pred = np.array([1.5, 2.2])
evaluate_result(y_true, y_pred)

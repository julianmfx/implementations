import numpy as np

# Adjust input to list and float
# Sigmoid function is
# o(x) = 1 / 1 + e^-x
# Decomposition
# 1. compute -x
# 2. compute e^-x
# 3. compute 1 + (e^-x)
# 4. compute 1 / (1 + (e^-x))


def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    Arguments:
        x: a number (float type) or a list of numbers

    Return:
        A float number or a numpy array
    """
    # transform the input into a array
    x = np.array(x)
    result = 1 / (1 + np.exp(-x))
    return result

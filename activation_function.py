import numpy as np

class ActivationFunction:
    """step sigmoid """
    def step_function(x):
        y = x > 0
        return y.astype(np.int)


    
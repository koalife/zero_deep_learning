import numpy as np

class ActivationFunction:
    """step sigmoid relu"""
    def step_function(x):
        y = x > 0
        return y.astype(np.int)
    
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    def relu(x):
        return np.maximum(0,x)
    
    def identity_function(x):
        return x
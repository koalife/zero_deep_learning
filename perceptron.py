import numpy as np

class Perceptron:
    """ AND, NAND, OR, XOR""" # comment

    def AND(x1, x2):
        x = np.array([x1,x2])
        w = np.array([0.5, 0.5])
        b = -0.7
        tmp = np.sum(w*x) + b
        if tmp <= 0:
            return 0
        else:
            return 1
    
    def NAND(x1, x2):
        x = np.array([x1, x2])
        w = np.array([-0.5, -0.5])
        b = 0.7
        tmp = np.sum(w*x) + b
        if tmp <= 0:
            return 0
        else:
            return 1

    def OR(x1, x2):
        x = np.array([x1, x2])
        w = np.array([0.5,0.5])
        b = -0.2
        tmp = np.sum(x*w) + b
        if tmp <= 0:
            return 0
        else:
            return 1
    
    def XOR(x1,x2):
        s1 = self.NAND(x1,x2)
        s2 = self.OR(x1,x2)
        y = self.AND(s1,s2)
        return y


import matplotlib.pyplot as plt
import numpy as np

class Particle:
    def __init__(self, v_0, kut, x_0):
        self.v_0 = v_0
        self.kut = kut
        self.x_0 = x_0 
    
    def reset(self):
        self.v_0 = 0
        self.kut = 0
        self.x_0 = 0


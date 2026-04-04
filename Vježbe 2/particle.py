import matplotlib.pyplot as plt
import numpy as np

class Particle:
    def __init__(self, v_0, kut, x_0=0, y_0=0 ):       #ako TI ne daš x0 i y0, Python automatski uzme 0
        
        self.kut = np.radians(kut)
        self.x_0 = x_0 
        self.y_0 = y_0
        self.x = x_0
        self.y = y_0

        self.g = 9.81

        self.v_0 = v_0
        self.vx = v_0 * np.cos(kut)
        self.vy = v_0 * np.sin(kut)

        self.x_list = [self.x]
        self.y_list = [self.y]

    def reset(self):

        self.vx = self.v_0 * np.cos(self.kut)
        self.vy = self.v_0 * np.sin(self.kut)
        self.x = self.x_0
        self.y = self.y_0
        self.x_list = [self.x]
        self.y_list = [self.y]

        
    def __move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.vy -= self.g * dt 

        self.x_list.append(self.x)
        self.y_list.append(self.y)

    def range(self, dt= 0.01):
        self.reset()

        while self.y >= 0 or self.vy >= 0:
            self.__move(dt)
        
        return self.x
    
    def plot_trajectory(self, dt=0.01):
        self.reset()

        while self.y >= 0 or self.vy >= 0:
            self.__move(dt)

        plt.plot(self.x_list, self.y_list)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.show()
        
# p = Particle(10, 45, 0, -1)
# print(p.range())       


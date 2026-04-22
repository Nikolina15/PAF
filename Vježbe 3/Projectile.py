import numpy as np
import matplotlib.pyplot as plt

class Projectile:

    def __init__(self, v0, theta, k=0.1, m=1):
        self.v0 = v0
        self.theta = theta
        self.k = k
        self.m = m
        self.g = 9.81

        self.reset()

    def reset(self):
        self.x = 0
        self.y = 0
        self.vx = self.v0 * np.cos(self.theta)
        self.vy = self.v0 * np.sin(self.theta)

        self.x_list = [self.x]
        self.y_list = [self.y]

    def move(self, dt):
        # ubrzanja
        ax = -(self.k / self.m) * self.vx
        ay = -self.g - (self.k / self.m) * self.vy

        # Euler update
        self.vx += ax * dt
        self.vy += ay * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

        self.x_list.append(self.x)
        self.y_list.append(self.y)

    def simulate(self, dt):
        self.reset()

        while self.y >= 0:
            self.move(dt)

        return self.x_list, self.y_list
    
    def move_RK4(self, dt):

        def ax(vx):
            ax = -(self.k / self.m) * vx
            return ax
        
        def ay(vy):
            ay = -self.g - (self.k / self.m) * vy
            return ay
        
        #prvi nagib (k1), nagib ce biti derivacija u toj tocki
        k1_vx = ax(self.vx)
        k1_vy = ay(self.vy)
        k1_x = self.vx
        k1_y = self.vy

        # k2 (nagib na sredini td/2)
        vx2 = self.vx + k1_vx * dt/2
        vy2 = self.vy + k1_vy * dt/2

        k2_vx = ax(vx2)
        k2_vy = ay(vy2)
        k2_x = vx2
        k2_y = vy2

        # k3 (sredina)
        vx3 = self.vx + k2_vx * dt/2
        vy3 = self.vy + k2_vy * dt/2

        k3_vx = ax(vx3)
        k3_vy = ay(vy3)
        k3_x = vx3
        k3_y = vy3

        # k4 (nagib na kraju)
        vx4 = self.vx + k3_vx * dt
        vy4 = self.vy + k3_vy * dt

        k4_vx = ax(vx4)
        k4_vy = ay(vy4)
        k4_x = vx4
        k4_y = vy4

        self.vx += dt/6 * (k1_vx + 2*k2_vx + 2*k3_vx + k4_vx)
        self.vy += dt/6 * (k1_vy + 2*k2_vy + 2*k3_vy + k4_vy)

        self.x += dt/6 * (k1_x + 2*k2_x + 2*k3_x + k4_x)
        self.y += dt/6 * (k1_y + 2*k2_y + 2*k3_y + k4_y)

        self.x_list.append(self.x)
        self.y_list.append(self.y)

    def simulate_RK4(self, dt):
        self.reset()

        while self.y >= 0:
            self.move_RK4(dt)
        
        return self.x_list, self.y_list
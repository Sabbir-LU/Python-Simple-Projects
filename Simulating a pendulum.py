# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:02:50 2024

@author: ahmed
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.8       # Gravity (m/s^2)
L = 2.0        # Length of the pendulum (m)
theta0 = np.pi / 4  # Initial angle (radians)

dt = 0.05  # Time step (s)

def theta(t, theta0, L, g):
    return theta0 * np.cos(np.sqrt(g / L) * t)


t_max = 10  #change duration
t = np.arange(0, t_max, dt)

theta_t = theta(t, theta0, L, g)

x = L * np.sin(theta_t)
y = -L * np.cos(theta_t)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-L - 0.1, L + 0.1)
ax.set_ylim(-L - 0.1, L + 0.1)

rod, = ax.plot([], [], 'o-', lw=2)
bob, = ax.plot([], [], 'o', color='red', markersize=10)

def init():
    rod.set_data([], [])
    bob.set_data([], [])
    return rod, bob


def update(frame):
    rod.set_data([0, x[frame]], [0, y[frame]])
    bob.set_data(x[frame], y[frame])
    return rod, bob

#animationing
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*1000)

plt.show()

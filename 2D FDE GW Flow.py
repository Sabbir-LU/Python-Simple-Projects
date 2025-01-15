# -*- coding: utf-8 -*-
"""
Created on Thu Sep  12 00:57:21 2023

@author: ahmed
"""

import numpy as np
import matplotlib.pyplot as plt

def groundwater_flow_fdm(nx, ny, Lx, Ly, K, R, tol=1e-6, max_iter=10000):

    dx = Lx / (nx - 1)
    dy = Ly / (ny - 1)  

    h = np.zeros((ny, nx))

    h[:, 0] = 10
    h[:, -1] = 5  
    h[0, :] = 10  
    h[-1, :] = 5  

    for it in range(max_iter):
        h_old = h.copy()

        for i in range(1, ny - 1):
            for j in range(1, nx - 1):
                h[i, j] = 0.25 * (h_old[i + 1, j] + h_old[i - 1, j] +
                                  h_old[i, j + 1] + h_old[i, j - 1] -
                                  R / K * dx**2)

        if np.max(np.abs(h - h_old)) < tol:
            print(f"Converged after {it} iterations.")
            break
    else:
        print("Maximum iterations reached without convergence.")

    return h

# Parameters
domain_length_x = 100
domain_length_y = 100
grid_points_x = 50
grid_points_y = 50
hydraulic_conductivity = 10
recharge_rate = 0.001

hydraulic_head = groundwater_flow_fdm(
    grid_points_x, grid_points_y,
    domain_length_x, domain_length_y,
    hydraulic_conductivity, recharge_rate
)

# Plot
x = np.linspace(0, domain_length_x, grid_points_x)
y = np.linspace(0, domain_length_y, grid_points_y)

plt.imshow(hydraulic_head, extent=(0, domain_length_x, 0, domain_length_y), origin="lower", cmap="viridis")
plt.colorbar(label="Hydraulic Head (m)")
plt.title("Hydraulic Head Distribution (Steady State)")
plt.xlabel("Distance (m)")
plt.ylabel("Distance (m)")
plt.show()
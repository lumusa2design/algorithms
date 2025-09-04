from cProfile import label

import matplotlib.pyplot as plt
import numpy as np


def montecarlo_pi_aproximation(N=1000):
    np.random.seed(3141)
    x_axis, y_axis = np.random.uniform(-1,1,size=(2,N))
    inside =  (x_axis**2 + y_axis**2) <= 1
    pi_hat = inside.sum() * 4 /N
    porcentual_error = abs((pi_hat - np.pi)/np.pi)

    plt.figure(figsize=(8,8))
    plt.scatter(x_axis[inside], y_axis[inside], s=3,c='blue', label="inside the circle")
    plt.scatter(x_axis[~inside], y_axis[~inside], s=3,c='red', label="out of the circle")

    circle = plt.Circle((0, 0), 1, fill=False, linewidth=2, color='k')
    ax = plt.gca()
    ax.add_artist(circle)

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.axis('square')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'N = {N}  |  pi = {pi_hat:.6f}  |  error = {porcentual_error:.4f}%')
    plt.legend(frameon=True, framealpha=0.9, fontsize=11)
    plt.show()


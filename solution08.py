# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>08.py
#
import numpy as np
import matplotlib.pylab as plt

# Exercise 1
#
def exercise1():
    """
    Fourier decomposition of the sawtooth wave. 
    """
    # close all figures
    plt.close('all')
    plt.rc('font', size=12)

    # Task 1A: Write a function that evaluates the sawtooth signal over a single period
    #
    def sawtooth_period(x):
        f = x / np.pi - 1
        f[np.isclose(x, 0.0)] = 0.0
        return f

    # Task 1B: Generalize the implementation of the sawtooth signal by using the modulo
    # operation `np.mod` with a period of 2 pi before you call `sawtooth_period`
    #
    def sawtooth(x):
        return sawtooth_period(np.mod(x, 2 * np.pi))
    
    # Task 1C: Evaluate the sawtooth signal over the interval [-pi, 4*pi] using 101
    # sampling points. Plot the signal using a 2D line plot: 
    #
    x = np.linspace(-np.pi, 4 * np.pi, 101)
    f = sawtooth(x)

    xticks = np.linspace(-pi, 4 * np.pi, 6)
    xticklabels = ['$-\pi$', '0', '$\pi$', '$2\pi$', '$3\pi$', '$4\pi$']
    
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.plot(x, f, color='r', lw=3)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.grid()
    fig.tight_layout()

    # Task 1D: Evaluate and plot the Fourier sum for m=1, 2, 3, 4, 5
    #
    figD, ax = plt.subplots(figsize=(6, 2))
    ax.plot(x, f, color='r', lw=3)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.grid()
    figD.tight_layout()

    f_m = 0.0
    for k in range(1, 6):
        f_m += - 2 / np.pi * np.sin(k * x) / k
        ax.plot(x, f_m)
    
    # Task 1E: Evaluate and plot the Fourier sum for m=1000
    #
    for k in range(6, 1001):
        f_m += - 2 / np.pi * np.sin(k * x) / k
        
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.plot(x, f, color='r', lw=6)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    ax.grid()
    ax.plot(x, f_m, color='k')
    fig.tight_layout()
    
    # Task 1F: Add a legend to the plot created in 1D
    #
    figD.axes[0].legend(['sawtooth'] + [rf'$m={i}$' for i in range(1, 6)], fontsize=8)
    figD.tight_layout()

    
# Exercise 2
#    
def exercise2():
    
    # close all figures
    plt.close('all')
    plt.rc('font', size=10)
    
    # Task 2A: create a 3D line plot of a sine wave with increasing phase and amplitude
    #
    t = np.linspace(0, 5 * np.pi, 201)
    fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
    for phi in np.linspace(0, np.pi, 11):
        f = (1 + 2 * phi / np.pi) * np.sin(t + phi)
        ax.plot(t, np.full(t.shape, phi), f)

    ax.set_xticks(np.arange(6) * np.pi)
    ax.set_xticklabels(['0', '$\pi$', '$2\pi$', '$3\pi$', '$4\pi$', '$5\pi$'])
    ax.set_xlim(0.0, 5 * np.pi)
    ax.set_xlabel(r'$t$')
    ax.set_yticks(np.linspace(0.0, 1.0, 3) * np.pi)
    ax.set_yticklabels(['0', '$\pi/2$', '$\pi$'])
    ax.set_ylim(0.0, np.pi)
    ax.set_ylabel(r'$\varphi$')
    ax.set_zticks([-4, -2, 0, 2, 4])
    ax.set_zlim(-4, 4)
    ax.set_zlabel(r'$f(t, \varphi)$')
    ax.view_init(elev=45.0)

    # Task 2B: create a side view by either using `ax.view_init`
    #
    ax.view_init(elev=0., azim=-90.)

    # Task 2C: create a side view by generating a new 2D line plot
    #
    fig2, ax2 = plt.subplots(figsize=(5, 4))
    for phi in np.linspace(0, np.pi, 11):
        f = (1 + 2 * phi / np.pi) * np.sin(t + phi)
        ax2.plot(t, f)
    ax2.set_xticks(ax.get_xticks())
    ax2.set_xticklabels(ax.get_xticklabels())
    ax2.set_xlim(ax.get_xlim())
    ax2.set_xlabel(ax.get_xlabel())
    ax2.set_yticks(ax.get_zticks())
    ax2.set_ylim(ax.get_zlim())
    ax2.set_ylabel(ax.get_zlabel())
    fig2.tight_layout()

    
# Exercise 3
#    
def exercise3():

    # close all figures
    plt.close('all')
    plt.rc('font', size=14)

    # Task 3A: create a bw image with a white square in the middle
    #
    image = np.zeros((100, 100), dtype=bool)
    image[25:75, 25:75] = True

    # Task 3B: create a 8-bit image with increasing brighter squares on the diagonal
    #
    image2 = np.zeros((500, 500), dtype=np.uint8)
    for i in range(1, 11):
        s = slice((i-1) * 50, i * 50)
        image2[s, s] += i * 25
        
    # Task 3C: plot the images created in 3A and 3B side by side
    #
    kw = dict(xticks=[], yticks=[])
    fig, ax = plt.subplots(1, 2, figsize=(8, 4), subplot_kw=kw)
    ax[0].imshow(image, cmap='gray')    
    ax[1].imshow(image2, cmap='gray')
    fig.tight_layout()

    
if __name__ == '__main__':
    exercise1()
    exercise2()
    exercise3()

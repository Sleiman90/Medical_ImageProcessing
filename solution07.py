# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>07.py
#

# useful imports
import numpy as np
import matplotlib.pyplot as plt


### Exercise 1: 2D plot
#
def exercise1():
    """
    My first plot. 
    """
    # close all figures
    plt.close('all')

    # set fontsize to 16
    plt.rc('font', size=16)

    # create a new figure with a single subplot
    fig, ax = plt.subplots()

    # Task 1A: plot x against y1 = sin(10*x) * exp(-x/2) as blue line
    x = np.arange(0, 3 * np.pi, 0.02)
    y1 = np.sin(10 * x) * np.exp(-x / 2)
    ax.plot(x, y1, color='b')
    
    # Task 1B: plot envelope functions in red and greed
    y2 = np.exp(-x / 2)
    ax.plot(x, y2, color='r')
    ax.plot(x, -y2, color='g')

    # Task 1C: set axis limits
    ax.set_xlim(0, 3 * np.pi)
    ax.set_ylim(-1.2, 1.2)

    # Task 1D: show grid
    ax.grid(True)

    # Task 1E: set xticks
    ax.set_xticks(np.pi * np.arange(4))

    # Task 1F: change tick labels
    ax.set_xticklabels(['0', '$\pi$', '$2\pi$', '$3\pi$'])

    # Task 1G: set title
    ax.set_title('My first plot')

    # Task 1H: x and y labels
    ax.set_xlabel('x-axis [x-units]')
    ax.set_ylabel('y-axis [y-units]')

    # Task 1I: add a legend
    ax.legend([r'$\sin(10x)e^{-x/2}$', r'$e^{-x/2}$', r'$-e^{-x/2}$'])
    
    # Task 1J: save figure as PNG file
    fig.tight_layout()
    fig.savefig('/tmp/MyFirstPlot.png')
    
    return fig, ax


### Exercise 2: 2D plot with two different y-axes
#
def exercise2():
    
    # close all figures
    plt.close('all')
    
    # set fontsize to 16
    plt.rc('font', size=16)

    # Task 2A
    h0 = 100.0 # m
    g = 9.81 # m / s**2
    tmax = np.sqrt(2 * h0 / g)
    t = np.linspace(0., tmax, 100)
    
    h = h0 - 0.5 * g * t**2
    v = g * t

    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    ax.plot(t, h, color='r')
    ax2.plot(t, v, color='b')
    
    # Task 2B
    ax.set_xlabel('time [s]')
    ax.set_ylabel('height [m]', color='r')
    ax2.set_ylabel('velocity [m/s]', color='b')
    ax.set_title('Freely falling object')
    
    # Task 2C
    ax.set_xlim(0, tmax)
    ax.set_ylim(0, None)
    ax2.set_ylim(0, None)
    fig.tight_layout()
    fig.savefig('/tmp/FreeFall.png')
    
    return fig, ax


### Exercise 3: Parameteric plots
#
def exercise3():

    # keyword figsize determines height and width of figure
    # setting figsize here to ensure that plot has square shape
    fig, ax = plt.subplots(figsize=(5, 5))

    # Task 3A: plot a full circle
    phi = np.linspace(0., 2 * np.pi, 100)
    r = 10.
    x, y = np.array([np.cos(phi), np.sin(phi)])
    ax.plot(r * x, r * y)
    
    # Task 3B: plot full circles at different centers
    for cx, cy in [(4., 3.5), (-4., 3.5), (0., -1.5)]:
        ax.plot(x + cx, y + cy)
    
    # Task 3C: circle segment
    phi = np.linspace(-3, -1, 100) * 0.25 * np.pi
    x, y = 8 * np.array([np.cos(phi), np.sin(phi)])
    cx, cy = 0., 1.5
    ax.plot(x + cx, y + cy)
    
    return fig, ax


if __name__ == '__main__':
    fig, ax = exercise1()
    fig, ax = exercise2()
    fig, ax = exercise3()

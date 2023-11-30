# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>09.py
#
import numpy as np
import matplotlib.pylab as plt

# some nice colors
colors = [(.85, .3, .1), (.15, .35, .6), (.95, .7, 0.1), (.0, .0, .0), (.8, .8, .8)]

# Exercise 1: NumPy warmup
#
def exercise1():

    a = np.array([[ 7,  4,  1, 11],
                  [ 3, 10,  2, -8],
                  [ 6,  9,  0,  5]])
    
    # Task 1A: Find and print the minimum value of 'a' by using a NumPy function
    #
    print('Task 1A:', np.min(a))

    # Task 1B: Print the row and column index of the smallest entry in 'a' by using
    # NumPy functions
    #
    print('Task 1B:', np.unravel_index(np.argmin(a), a.shape))
    
    # Task 1C: Create and print the matrix \cos(2\pi m n/N) for N=6 and
    # n, m in {0, 1, ..., 5}
    #
    N = 6
    m = n = np.arange(N)
    C = np.cos(2 * np.pi * np.multiply.outer(n, m) / N)
    print('Task 1C:\n', C)

    # Task 1D: Evaluate and print the given polynomial at x=0, 1, 2, 3, 4, 5, 6
    #
    f = lambda x : -1 + 2 * x - 3 * x**2 + 4 * x**3
    print('Task 1D:\n', f(np.arange(6)))

# Exercise 2: Matplotlib warmup
#
def exercise2():

    phi = np.linspace(0, 2 * np.pi, 100, endpoint=False) # angles
    r = 1 + np.mod(phi, 2*np.pi/6) # radii

    # Task 2A: form two arrays name 'x' and 'y' with x and y coordinates
    #
    x = r * np.cos(phi)
    y = r * np.sin(phi)

    # Task 2B: form a complex array with real part x and imaginary part y
    #
    z = x + 1j * y

    # Task 2C: rotate the point pattern by 30 degrees using that fact that a rotation
    # in 2D is equivalent to a multiplication with a complex number whose phase is the
    # rotation angle
    #
    phase = np.exp(1j * np.deg2rad(30))
    z_rot = z * phase

    # Task 2D: show both points patterns, unrotated and rotated, as scatter plots using
    # different colors
    #
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.scatter(z.real, z.imag, color=colors[0])
    ax.scatter(z_rot.real, z_rot.imag, color=colors[1])
    fig.tight_layout()

# Exercise 3
#
def exercise3():

    # close all figures
    plt.close('all')

    # example system but your code could should also work for other choices
    # of A and b
    A = np.array([[2, 4], [-1, 7]])
    b = np.array([10, 4])

    # Task 3A: plot both lines representing row picture
    x = np.linspace(-10, 10, 10)
    lines = [(b - a[0] * x) / a[1] for a, b in zip(A, b)]
    fig, axes = plt.subplots(1, 2, figsize=(8, 3), sharex=True, sharey=True)
    for ax in axes:
        for color, y in zip(['r', 'b'], lines):
            ax.plot(x, y, lw=3, alpha=0.7, color=color)
        ax.set_xlabel('$x$')
        ax.set_ylim(-2, 7)
        ax.set_xlim(-10., 10)
    axes[0].set_ylabel('$y$')

    # Task 3B: compute the solution and show it as dot as well as explicit numbers in
    # the subplot title
    Ainv = np.array([[A[1, 1], -A[0, 1]],
                     [-A[1, 0], A[0, 0]]])
    Ainv = Ainv / (A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])
    x, y = Ainv @ b

    axes[1].scatter(x, y, s=200, color='k', zorder=3)
    axes[1].set_title(f'$x_1={x:.1f}$, $x_2={y:.1f}$')
    fig.tight_layout()

# Exercise 4
#
def exercise4():
    """Solving a system of linear equations."""

    A = np.array([[2, 3, 1],
                  [1, 1, 1],
                  [5, -1, 10]])

    b = np.array([11, 6, 34])

    x = np.linalg.inv(A) @ b

    assert np.allclose(A @ x, b)

    return x


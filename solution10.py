# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>10.py
#
import numpy as np
import matplotlib.pylab as plt

def generate_straightline_data(theta, N=10, sigma=1.0):
    """Generate toy data for a given set of straight line parameters theta whose
    elements are

    * theta[0] : intercept / y-axis offset
    * theta[1] : slope

    Additional parameters:
    * N : number of data points
    * sigma : standard deviation of Gaussian errors
    """
    # set random seed for comparability
    np.random.seed(1234)

    # linearly sampled inputs
    x = np.linspace(-10., 10., N)
    
    # generate Gaussian errors
    eps = np.random.normal(0., sigma, size=N)

    # noisy data
    y = theta[0] + theta[1] * x + eps

    return x, y

# Please do not change the code above this line

# Exercise 1: Fitting a single linear parameter
#
def exercise1():
    """Estimation of a single linear parameter. """
    
    # close all figures
    plt.close('all')
    plt.rc('font', size=14)

    # Task 1A: Implement a heuristic estimator
    #
    def heuristic(x, y, f):
        """x, y: inputs/outputs; f: callable"""
        return np.sum(y) / np.sum(f(x))

    # Task 1B: Implement the least-squares estimator
    #
    def least_squares(x, y, f):
        """x, y: inputs/outputs; f: callable"""
        F = f(x)
        return (F.T @ y) / (F.T @ F)

    # Task 1C: Apply both estimators to the data above and plot them
    #
    x = np.array([0., 1., 2., 3., 4., 5., 6.])
    y = np.array([10.236,  3.083,  2.07 ,  0.342, -0.177,  0.511,  0.455])

    def f(x):
        return np.exp(-x)
    
    theta1A = heuristic(x, y, f)
    theta1B = least_squares(x, y, f)
    x_fine = np.linspace(x.min(), x.max(), 10 * len(x))
    fig, axes = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)
    for ax, theta, title in zip(
        axes, [theta1A, theta1B], ['Heuristic', 'Least-squares']
    ):
        ax.set_title(title + rf' ($\hat\theta$={theta:.2f})')
        ax.scatter(x, y, color='k', alpha=0.7, s=100)
        ax.plot(x_fine, theta * f(x_fine), color='r', lw=3, alpha=0.7)
        ax.set_xlabel('inputs $x_n$')
    axes[0].set_ylabel('outputs $y_n$')
    fig.tight_layout()

    
# Exercise 2: straight line fitting
#    
def exercise2():
    
    # close all figures
    plt.close('all')

    # true parameters (slope, intercept)
    theta_true = (1.3, 0.7)
    x, y = generate_straightline_data(theta_true, sigma=2.)
    
    # Please do not touch the code above this line

    # Task 2A: Fit a straight line to (x, y) using the equations derived in the lecture.
    #
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    v_x, v_xy = np.cov(x, y)[0]

    theta2A = np.array([np.mean(y) - np.mean(x) * v_xy / v_x, v_xy / v_x])
    
    # Task 2B: Estimate the parameters with the general formalism. Build the design
    # matrix 'F' and compute the best fitting slope and intercept
    # 
    F = np.transpose([np.ones_like(x), x])
    theta2B = np.linalg.pinv(F) @ y

    # Task 2C: Implement a local function 'calc_chi2' that computes the least-squares
    # loss for a given intercept (1st argument) and slope (2nd argument)
    #
    def calc_chi2(theta):
        return np.sum(np.square(y - theta[0] - theta[1] * x))

    # Task 2D: Fit a straight line with a grid search.
    #
    range1, range2 = (-1, 3), (0, 2)
    theta1, theta2 = np.linspace(*range1, 21), np.linspace(*range2, 31)
    chi2 = np.array([calc_chi2([a, b]) for a in theta1 for b in theta2])
    i, j = np.unravel_index(np.argmin(chi2), (len(theta1), len(theta2)))
    theta2D = [theta1[i], theta2[j]]
    
    # Task 2E: Fit a straight line with a random search.
    #
    theta2E = None
    for _ in range(100):
        theta = [np.random.uniform(*range1), np.random.uniform(*range2)]
        if theta2E is None or calc_chi2(theta) < calc_chi2(theta2E):
            theta2E = theta
    
    # Task 2F: Plot the data, the true straight line and the lines estimated in Tasks
    # 2A, 2B, 2D, 2E
    #
    plt.rc('font', size=10)
    fig, axes = plt.subplots(2, 2, figsize=(6, 4), sharex=True, sharey=True)
    for ax, theta, task in zip(
        axes.flat, [theta2A, theta2B, theta2D, theta2E], 'ABDE'
    ):
        ax.set_title(rf"$\hat\theta$=({theta[0]:.2f}, {theta[1]:.2f}) (Task 2{task})")
        ax.scatter(x, y, color='k', alpha=0.7)
        ax.plot(x, theta_true[0] + theta_true[1] * x, color='r', ls='--', alpha=0.8,
                label="correct model")
        ax.plot(x, theta[0] + theta[1] * x, color='k', alpha=0.5,
                label="estimated model")
    for ax in axes[-1]:
        ax.set_xlabel('$x$')
    for ax in axes[:, 0]:
        ax.set_ylabel('$y$')
    fig.tight_layout()

    
# Exercise 3: estimating a straight line modulated by a sinusoidal perturbation
#
def exercise3():
    
    # close all figures and set random seed
    plt.close('all')
    np.random.seed(1234)
    
    # Task 3A: implement a local function 'f(x, theta)' that computes the modulated
    # straight line for given inputs 'x' and parameters 'theta' where theta[0] is the
    # intercept, theta[1] the slope, theta[2] the amplitude and theta[3] the phase
    #
    def f(x, theta):
        return theta[0] + theta[1] * x + theta[2] * np.sin(x + theta[3])

    # Task 3B: generate 50 data points covering 2.5 cycles of the sinusoidal
    # perturbation with an intercept=1.0, a slope=2.0, an amplitude=5.0 and a phase=0.7
    # assuming identical Gaussian errors with standard deviation sigma=3.0
    #
    N = 50
    x = np.linspace(0., 2 * np.pi, N) * 2.5
    theta_true = [1.0, 2.0, 5.0, 0.7]
    sigma = 3.0
    eps = np.random.normal(0., sigma, N)
    y = f(x, theta_true) + eps
    
    # Task 3C: implement a local function "calc_chi2(theta)" that computes the
    # least-squares loss.

    def calc_chi2(theta):
        return np.sum(np.square(y - f(x, theta)))

    # Task 3D: fit the model by estimating the linear paramters for ten phases in the
    # interval [0, pi) and store the parameters that achieve the best chi2.
    #
    theta3D = None
    for phase in np.linspace(0.0, np.pi, 10, endpoint=False):
        F = np.transpose([np.ones(N), x, np.sin(x + phase)])
        theta = np.append(np.linalg.pinv(F) @ y, phase)
        if theta3D is None or calc_chi2(theta) < calc_chi2(theta3D):
            theta3D = theta
    
    # Task 3E: estimate the parameters of the linear model obtained by applying the
    # trigonometric identity and using the least-squares estimator; map the modified
    # parameters back to the original parameters.
    #
    F = np.transpose([np.ones(N), x, np.sin(x), np.cos(x)])
    theta3E = np.linalg.pinv(F) @ y
    a, b = theta3E[-2:]
    theta3E[2:] = np.sqrt(a**2 + b**2), np.arctan2(b, a)

    # Task 3F: plot the data, the true and the estimated models obtained in 3D and 3E
    # using Matplotlib
    #
    plt.rc('font', size=10)
    fig, axes = plt.subplots(2, 1, figsize=(5, 5), sharex=True, sharey=True)
    for ax, theta, task in zip(axes, [theta3D, theta3E], ["D", "E"]):
        ax.set_title(f"theta={np.round(theta,2)} (Task 3{task})")
        ax.scatter(x, y, color='k', alpha=0.7)
        ax.plot(x, f(x, theta_true), color='r', ls='--', alpha=0.8,
                label="correct model")
        ax.plot(x, f(x, theta), color='k', alpha=0.5, label="estimated model")
        ax.legend()
    axes[1].set_xlabel('$x$')
    for ax in axes:
        ax.set_ylabel('$y$')
    fig.tight_layout()

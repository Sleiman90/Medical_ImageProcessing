# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>11.py
#
import numpy as np
import matplotlib.pylab as plt
import scipy.optimize as opt

def generate_exponential_data(theta, N=10, sigma=1.0):
    """Generate toy data for a given amplitude and rate:

    * theta[0] : amplitude
    * theta[1] : rate

    Additional parameters:
    * N : number of data points
    * sigma : standard deviation of Gaussian errors
    """
    # set random seed for comparability
    np.random.seed(1234)

    # linearly sampled inputs
    x = np.linspace(0., 1., N) * 10 / theta[1]

    # generate Gaussian errors
    eps = np.random.normal(0., sigma, size=N)

    # noisy data
    y = theta[0] * np.exp(-theta[1]*x) + eps

    return x, y

# Please do not change the code above this line

# Exercise 1: fitting an exponential signal
#    
def exercise1():
    
    # close all figures
    plt.close('all')

    # generate data for the given amplitude and rate
    theta_true = (10., 0.5)                                 # correct model
    x, y = generate_exponential_data(theta_true, sigma=0.5) # data
    
    # Please do not change the code above this line

    # Task 1A: Estimate the parameters of the log-transformed model with a straight
    # line fit and transform the fitted parameters back to the original parameters
    # (amplitude, rate). 
    #
    slope, intercept = np.polyfit(x[y > 0], np.log(y[y > 0]), 1)
    thetaA = [np.exp(intercept), -slope]
    
    # Task 1B: Implement a local function "calc_chi2(theta)" that computes the least-
    # squares loss for a given theta where theta[0] is the amplitude and theta[1] is
    # the rate.
    #
    def f(x, theta):
        return theta[0] * np.exp(-theta[1] * x)
    
    def calc_chi2(theta):
        return np.sum(np.square(y - f(x, theta)))

    # Task 1C: Fit the parameters of the exponential model with the Nelder-Mead
    # algorithm offered by scipy.optimize starting from the values obtained in task 1A
    # (or from [1., 1.])
    #
    result = opt.minimize(calc_chi2, [1., 1.], method='Nelder-Mead')
    thetaC = result.x

    # Task 1D: Plot the data, the true exponential model and the estimated models (from
    # tasks 1A and 1C) in two subplots. 
    #
    x_fine = np.linspace(x.min(), x.max(), 10 * len(x))
    plt.rc('font', size=10)
    fig, axes = plt.subplots(1, 2, figsize=(7, 3), sharex=True, sharey=True)
    for ax, theta, task in zip(axes, [thetaA, thetaC], 'AC'):
        ax.set_title(rf"$\hat\theta=${np.round(theta, 2)} (Task 1{task})")
        ax.scatter(x, y, color='k', s=100, alpha=0.7)
        ax.plot(x_fine, f(x_fine, theta_true), color='r', ls='--', lw=4, 
                label='true model')
        ax.plot(x_fine, f(x_fine, theta), color='k', label='fitted model', alpha=0.7,
                lw=2)
        ax.set_xlabel(r'$x$')
        ax.legend()
    axes[0].set_ylabel(r'$y$')
    fig.tight_layout()

    
# Exercise 2: fitting the Michaelis-Menten model
#
def exercise2():
    
    # close all figures
    plt.close('all')
    plt.rc('font', size=14)

    # data
    # x: substrate concentration
    x = np.array([0, 1, 2, 5, 8, 12, 30, 50])
    # y: velocity of product formation / reaction rate
    y = np.array([0, 11.1, 25.4, 44.8, 54.5, 58.2, 72.0, 60.1])

    # homogeneous error
    sigma = 4.5
    
    # Please don't change the code above this line
    
    # Task 2A:Implement the Michaelis-Menten model
    def michaelis_menten(x, theta):
        """Michaelis-Menten model

        Parameters
        ----------
        x: substrate concentrations

        theta: model parameters
        * theta[0]: maximum velocity
        * theta[1]: Michaelis constant

        Returns
        -------
        numpy array : predicted velocity / rate of reaction
        """
        return theta[0] * x / (theta[1] + x)

    # plot the data and the three models in a single plot
    models = [(100.40, 7.58), # model 1
              (66.80, 2.53),  # model 2
              (76.57, 4.37)]  # model 3
    x_fine = np.linspace(0., x.max(), 10 * len(x))
    fig, ax = plt.subplots()
    for i, theta in enumerate(models):
        ax.plot(x_fine, michaelis_menten(x_fine, theta), label=f"model {i}", lw=3,
                alpha=0.8)
    ax.scatter(x, y, s=100, color='k', alpha=0.7)
    ax.set_xlabel("substrate concentration $x_n$")
    ax.set_ylabel("velocity $y_n$")
    ax.legend()
    fig.tight_layout()

    # Task 2B: Implement the reduced chi2 loss as a local Python function.
    #
    def reduced_chi2(theta):
        residuals = y - michaelis_menten(x, theta)
        return 1 / (len(x) - len(theta)) * np.sum(np.square(residuals)) / sigma**2

    # Evaluate the reduced chi2 value for each of the three models and print it to the
    # console.
    #
    for i, theta in enumerate(models):
        print(f"model {i}: theta={np.round(theta, 2)}, " 
              f"reduced chi2={reduced_chi2(theta):.2f}")
    
    # Task 2C: Estimate the model parameters by transforming the data and fitting the
    # transformed data with a straight line. Possible choices: Lineweaver-Burk (1/x vs
    # 1/y), Hanes-Woolf (x vs x/y), or Eadie-Hofstee (-y/x vs y)
    #
    plt.rc("font", size=10)
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))
    
    # Lineweaver-Burk
    mask = ~np.isclose(x, 0.0) & ~np.isclose(y, 0.0)
    slope, intercept = np.polyfit(1 / x[mask], 1 / y[mask], 1)
    theta1 = 1 / intercept
    theta2 = slope * theta1
    theta_LB = [theta1, theta2]
    print(theta_LB)
    
    ax = axes[0]
    ax.set_title("Lineweaver-Burke\n" + f"{np.round(theta_LB, 3)}")
    ax.scatter(1 / x[mask], 1 / y[mask], s=100, color='k', alpha=0.7)
    ax.plot(1 / x[mask], intercept + slope / x[mask], color='r', ls='--',
                 label=f"{np.round([intercept, slope], 3)}")
    ax.legend(fontsize=10)
    ax.set_xlabel(r"$1/x$")
    ax.set_ylabel(r"$1/y$")    
    
    # Hanes-Woolf
    mask = ~np.isclose(y, 0.)
    slope, intercept = np.polyfit(x[mask], x[mask] / y[mask], 1)
    theta1 = 1 / slope
    theta2 = intercept * theta1
    theta_HW = [theta1, theta2]
    print(theta_HW)
    
    ax = axes[1]
    ax.set_title("Hanes-Wolf\n" + f"{np.round(theta_HW, 3)}")
    ax.scatter(x[mask], x[mask] / y[mask], s=100, color='k', alpha=0.7)
    ax.plot(x[mask], intercept + slope * x[mask], color='r', ls='--',
                 label=f"{np.round([intercept, slope], 3)}")
    ax.legend(fontsize=10)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$x/y$")    
    
    # Eadie-Hofstee
    mask = ~ np.isclose(x, 0.0)
    slope, intercept = np.polyfit(-y[mask] / x[mask], y[mask], 1)
    theta1 = intercept
    theta2 = slope
    theta_EH = [theta1, theta2]
    print(theta_EH)

    ax = axes[2]
    ax.set_title("Eadie-Hofstee\n" + f"{np.round(theta_EH, 3)}")
    ax.scatter(-y[mask] / x[mask], y[mask], s=100, color='k', alpha=0.7)
    ax.plot(-y[mask] / x[mask], intercept - slope * y[mask] / x[mask], color='r',
            ls='--', label=f"{np.round([intercept, slope], 3)}")
    ax.legend(fontsize=10)
    ax.set_xlabel(r"$-y/x$")
    ax.set_ylabel(r"$y$")    
    
    fig.tight_layout()
    
    # Task 2D: Fit the model by minimizing the reduced chi2 implemented in Task 2B by
    # using the Nelder-Mead algorithm
    # 
    theta2D = opt.minimize(reduced_chi2, models[0], method="Nelder-Mead").x
    print(theta2D)

    # Task 2E: Implement a loss function that depends only on theta2 by substituting
    # theta1 with its theta2-dependent least-squares estimate (Eq. 6 in homework). Plot
    # this function for logarithmically-spaced theta2 values. 
    #
    def g(theta2):
        return np.sum(x * y / (x + theta2)) / np.sum(x**2 / (x + theta2)**2)

    fun = lambda theta2: reduced_chi2([g(theta2), theta2])
    theta2 = np.logspace(-5, np.log10(20), 100)
    vals = list(map(fun, theta2))
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(theta2, vals, color="r", lw=3, alpha=0.7)
    ax.set_xlabel(r"Michaelis constant $\theta_2$")
    ax.set_ylabel(r"reduced $\widetilde\chi_r^2(\theta_2)$")
    fig.tight_layout()
    
    # Task 2F: Locate the best theta2 that minimizes the function implemented in the
    # previous task. From the estimate theta2, estimate theta1 using the theta2-
    # dependent least-squares estimate (Eq. 6 in homework). 
    #
    theta2 = theta2[np.argmin(vals)]
    theta1 = g(theta2)
    theta2F = [theta1, theta2]
    print(theta2F)
    
    # Task 2G: Update the plot generated in Task 2A by adding the models that you
    # determined in Tasks 2D and 2F
    #
    labels = [f"model {i}" for i in range(1, len(models) + 1)] + \
      ["Nelder-Mead", "1D grid search"]
    fig, ax = plt.subplots()
    for theta, label in zip(models + [theta2D, theta2F], labels):
        ax.plot(x_fine, michaelis_menten(x_fine, theta), label=label, lw=3,
                alpha=0.8)
    ax.scatter(x, y, s=100, color='k', alpha=0.7)
    ax.set_xlabel("substrate concentration $x_n$")
    ax.set_ylabel("velocity $y_n$")
    ax.legend()
    fig.tight_layout()

    
# Exercise 3: straight line fitting in the presence of an outlier
#    
def exercise3():

    # close all figures
    plt.close('all')
    plt.rc('font', size=14)

    # true (slope, intercept)
    theta_true = (1.3, 0.7)
    # errors
    sigma = np.array([1., 1., 1., 1., 1., 1., 1., 1., 1., 10.])
    # data
    x = np.linspace(-10., 10., 10)
    y = np.array([-5.23, -5.34, -1.16, -1.35, -0.2,
                  2.96, 4.49, 4.55, 6.76, -14.13])

    # Please don't change the code above this line
    
    # Task 3A: Estimate the intercept and slope assuming (wrongly) that the errors are
    # homogeneous. 
    #
    F = np.transpose([np.ones_like(x), x])
    theta3A = np.linalg.pinv(F) @ y
    
    # Task 3B: Estimate the straight line parameters using the general expression for
    # least-squares estimate 
    #
    A = F.T / sigma**2 @ F
    b = F.T / sigma**2 @ y
    theta3B = np.linalg.solve(A, b)
    
    # Task 3C: Plot the data, the true straight line and the estimated lines
    #
    title = "{0} errors: {1:.2f}, {2:.2f}"
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharex=True, sharey=True)
    for ax, theta, errtype in zip(
        axes, [theta3A, theta3B], ["homogeneous", "heterogeneous"]
    ):
        ax.set_title(title.format(errtype, *theta))
        ax.scatter(x, y, s=100, color='k', alpha=0.5)
        ax.plot(x, theta[0] + theta[1] * x, ls='-', label="estimated model", lw=4)
        ax.plot(x, theta_true[0] + theta_true[1] * x, ls='--', label="correct model",
                lw=4)
        ax.legend()
        ax.set_xlabel(r"$x$")
    axes[0].set_ylabel(r"$y$")
    fig.tight_layout()

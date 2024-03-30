import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['text.usetex'] = True # Enable LaTex

plt.style.use(['dark_background']) # Setting the style for the plot

# Function definition
def u_e(x): 
    return (-1/6)*(x**3) + (3/2)*x

def u_2(x):
    return (0.355*x)-(0.0625)*(x**2)

def u_3(x):
    return (1.6*x)-(0.25*(x**2))-(0.0005*(x**3))


x = np.linspace(0, 1, 100)  # Sample data.

# Plot configuration and visualization
plt.figure(figsize=(17, 13), layout="constrained")
plt.plot(x, u_3(x), '--', color='crimson', linewidth = 3.5, label=r'\texttt{Three-parameter\ Ritz\ Solution}, $\mathbf{U_3(x)=1.6x-0.25x^2-0.0005x^3}$') # Plot third order Ritz solution.
plt.plot(x, u_e(x), color='white', linewidth = 1.3, label=r'\texttt{Exact\ solution}, $\mathbf{u_e(x)=1.5x-0.166x^3}$')  # Plot the exact solution.
plt.plot(x, u_2(x), ':', color='orange', linewidth = 4, label=r'\texttt{Two-parameter\ Ritz\ Solution}, $\mathbf{U_2(x)=0.355x-0.0625x^2}$')  # Plot second order Ritz solution.

plt.xlabel(r"\bf{Coordinate} $x$", fontsize=28)
plt.ylabel(r'\bf{Variable} $u(x)$', fontsize=28)
plt.tick_params(labelsize=24)
plt.legend(loc=(0.03, 0.75), fontsize=24, labelcolor='linecolor')
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

def plot_constraints():
   
    fig, ax = plt.subplots(figsize=(8, 8))
    
    x = np.linspace(0, 7, 200)
 
    y1 = (11 - 2*x) / 6
    ax.plot(x, y1, label=r'$2x_1 + 6x_2 \leq 11$', color="blue")
    y2 = (6 - x) / 2
    ax.plot(x, y2, label=r'$x_1 + 2x_2 \leq 6$', color="green")
    
    # Set the limits of the plot
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 7)
    x_fill = np.linspace(0, 2.5, 200)
    y_fill1 = (11 - 2*x_fill) / 6
    y_fill2 = (6 - x_fill) / 2
    ax.fill_between(x_fill, np.minimum(y_fill1, y_fill2), 0, color='lightgray', alpha=0.5)
    ax.set_xlabel(r'$x_1$ (Chairs)')
    ax.set_ylabel(r'$x_2$ (Tables)')
    ax.grid(True)
    ax.legend(loc='best')
    
    return fig, ax, x

# Plot the constraints and feasible region
fig, ax, x = plot_constraints()
ax.plot(5.5, 0, 'ro', label='LP Relaxation Solution (5.5, 0)')
ax.plot(5, 0, 'go', label='Integer Optimal Solution (5, 0)', markersize=10)

plt.title('Feasible Region and Optimal Solution')
plt.show()

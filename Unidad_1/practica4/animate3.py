import itertools

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# set parameters
frames = 100
points = 20
np.random.seed(42)

# create data
data = np.random.rand(points, 2)

# set how the graph will change each frame
sizes = itertools.cycle([10, 50, 150])
colors = np.random.rand(frames, points)
colormaps = itertools.cycle(['Purples', 'Blues', 'Greens', 'Oranges', 'Reds'])
markers = itertools.cycle(['o', 'v', '^', 's', 'p'])

# init the figure
fig, ax = plt.subplots(figsize=(5,5))

def update(i):
    # clear the axis each frame
    ax.clear()

    # replot things
    ax.scatter(data[:, 0], data[:, 1],
               s=next(sizes),
               c=colors[i, :],
               cmap=next(colormaps),
               marker=next(markers))

    # reformat things
    ax.set_xlabel('world')
    ax.set_ylabel('hello')

ani = animation.FuncAnimation(fig, update, frames=frames, interval=500)
plt.show()
#ani.save('scatter.gif', writer='pillow')

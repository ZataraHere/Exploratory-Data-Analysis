import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from itertools import count

plt.style.use("seaborn-v0_8")

x = []
y = []
index = count()

def animate(i):
    x.append(next(index))
    y.append(np.random.randint(0, 5))
    plt.cla()
    plt.plot(x, y, marker="o")

ani = FuncAnimation(plt.gcf(), animate, interval=1000)  # Keep in variable
plt.show()  # Only ends after animation completes

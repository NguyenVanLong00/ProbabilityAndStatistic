import matplotlib.pyplot as plt
import numpy as np
# Data
x = np.arange(0, 6 * np.pi, 0.2)
y_1 = np.cos(x)
y_2 = np.sin(2 * x)
y_3 = y_1 + y_2

fig, axs = plt.subplots(3, 1, sharex = True)

print(type(fig))
print(type(axs))
axs[0].plot(x, y_1)
axs[1].plot(x, y_2)
axs[2].plot(x, y_3)
axs[0].set_ylabel('$y$')
axs[1].set_ylabel('$y$')
axs[2].set_ylabel('$y$')
axs[2].set_xlabel('$x$')

plt.show()
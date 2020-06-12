import numpy as np
import matplotlib.pyplot as plt



plt.figure()
### line plot 

### y = cos x

x = np.arange(0,4*np.pi/2,0.1)
y_sin = np.sin(x)

plt.subplot(3,2 , 1)
plt.plot(x,y_sin)
plt.xlabel('$x$')
plt.ylabel('$y$')

### y1 = 2^x | y2 = x^2

x = np.arange(1,10,1)
y_1 = 2**x
y_2 = x**2

plt.subplot(3,2 , 2)
plt.plot(x,y_1, label = '$2^x$' , color = 'g', linestyle = '-.' , marker = 's')
plt.plot(x,y_2, label = '$x^2$' , color = 'r', linestyle = '--' , marker = 'o')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.legend(loc = 'upper left')

plt.rc('font', size=10)          # controls default text sizes
plt.rc('axes', titlesize=10)     # fontsize of the axes title
plt.rc('axes', labelsize=12)     # fontsize of the x and y labels
plt.rc('xtick', labelsize=10)    # fontsize of the tick labels
plt.rc('ytick', labelsize=10)    # fontsize of the tick labels
plt.rc('legend', fontsize=10)    # legend fontsize

x = np.arange(-10, 10, 0.1)
y = x ** 3

plt.subplot(3,2 , 3)
plt.plot(x, y, label = '$x^3$')
plt.xlabel('$x$', fontsize = 12) # The fontsize can be set here as well
plt.ylabel('$y$', fontsize = 12)
plt.title('$y = x^3$', fontsize = 16) # Set title and its fontsize
plt.legend(loc = 'upper left')
plt.grid()

# Data
x = np.arange(0, 6 * np.pi, 0.2)
y_1 = np.cos(x)
y_2 = np.sin(2 * x)

# Plot y = cos(x) 

plt.subplot(3,2 , 4)
plt.plot(x, y_1, label = '$\cos(x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc = 'lower left')

# Plot y = sin(2x)
plt.subplot(3, 2, 4)
plt.plot(x, y_2, label = '$\sin(2x)$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc = 'lower left')
plt.show()


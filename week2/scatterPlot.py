import matplotlib.pyplot as plt 
import numpy as np 

# Data
x = np.arange(0, 10, 0.5) # x in [0, 10) 
noise = np.random.randn(len(x)) # Generate standard normal random variables
y = 2 * x + 3 + noise

plt.figure()
plt.scatter(x, y)
plt.plot(x, 2 * x + 3, color = 'r')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()
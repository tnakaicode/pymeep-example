import numpy as np
import matplotlib.pyplot as plt

px = np.linspace(-1, 1, 100)
py = np.sin(px)

plt.figure()
plt.plot(px, py)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20,90)
plt.plot(x,np.sin(x),label="Sine Wave")
plt.plot(x,np.cos(x),label="Cosine Wave")
plt.legend()
plt.show()
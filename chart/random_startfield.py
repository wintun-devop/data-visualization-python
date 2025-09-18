import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(500)*10
y = np.random.rand(500)*10
size=np.random.rand(500)*20
color=np.random.rand(500)

plt.scatter(x,y,s=size,c=color,cmap='twilight',alpha=0.8)
plt.axis('off')
plt.show()
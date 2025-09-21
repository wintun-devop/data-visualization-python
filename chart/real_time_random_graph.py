import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()
fig,ax = plt.subplots()
x =np.arange(0,50)
y =np.random.randint(1,10,50)
line , = ax.plot(x,y)
for _ in range(50):
    y=np.roll(y,-1)
    y[-1]=np.random.randint(1,10)
    line.set_ydata(y);fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.1)
plt.ioff();plt.show()



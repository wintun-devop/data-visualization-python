import matplotlib.pyplot as plt
import seaborn as sbn
import numpy as np

data = [np.random.normal(0,std,100) for std in range(1,4)]
print("data",data)
sbn.boxplot(data=data)
plt.title('Box Plot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
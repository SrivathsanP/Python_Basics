import matplotlib.pyplot as plt
import numpy as np

x = np.array([10,156])
y = np.array([20,322])

#adding text inside the plot
plt.text(60, 10, 'text inside graph ', fontsize = 22)

plt.plot(x,y, c='g')



plt.show()

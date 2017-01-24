import numpy as np
import matplotlib.pyplot as plt
import scipy.io

data = scipy.io.loadmat('./data/1D/var3.mat')
data = data['n']
plt.plot(data)
plt.show()

mean = np.mean(data) * np.ones(len(data))
var = np.var(data) * np.ones(len(data))
plt.plot(data, 'b-', mean, 'r-', mean-var, 'g--', mean+var, 'g--')
plt.grid()
plt.show()

plt.hist(data, bins=20)
plt.grid()
plt.show()
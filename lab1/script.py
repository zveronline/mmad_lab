import numpy as np
import matplotlib.pyplot as plt
import scipy.io

data = scipy.io.loadmat('./data/1D/var3.mat')
data = data['n']
mean = np.mean(data)*np.ones(len(data))
var = np.var(data)
plt.plot(data)
plt.show()
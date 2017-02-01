import numpy as np
import matplotlib.pyplot as plt
import scipy.io

data = scipy.io.loadmat('./data/1D/var3.mat')
data = data['n']
maxd = np.max(data)
mind = np.min(data)
median = np.median(data)
mean = np.mean(data)
s = np.std(data) #сред отклонение
var = np.var(data) #дисперсия
print(maxd, mind, median, mean, s, var)
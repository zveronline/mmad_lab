import numpy as np
import matplotlib.pyplot as plt
import scipy.io

def autocorrelate(a):
	n = len(a)
	cor = []
	for i in range(n//2, n//2+n):
		a1 = a[:i+1] if i < n else a[i-n+1:]
		a2 = a[n-i-1:] if i < n else a[:2*n-i-1]
		cor.append(np.corrcoef(a1, a2)[0, 1])
	return np.array(cor)

data = scipy.io.loadmat('./data/1D/var3.mat')
data = data['n']
data = np.ravel(data)
cor = autocorrelate(data)
plt.plot(cor)
plt.show()
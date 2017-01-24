import numpy as np
import matplotlib.pyplot as plt
import scipy.io

data = scipy.io.loadmat('./data/ND/var3.mat')
data = data['mn']
n = data.shape[1]
corr_matrix = np.zeros([n, n])
for i in range(0, n):
	row = data[i, :]
	for j in range(0, n):
		col = data[:, j]
		corr_matrix[i ,j] = np.corrcoef(col, row)
np.set_printoptions(precision=2)
print(corr_matrix)
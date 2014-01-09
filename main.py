import numpy as np

DATA_FILE = 'breast_cancer_fix'

X = np.loadtxt(DATA_FILE, delimiter=',')
y = X[:,1]
X = np.delete(X, 1, 1)

print X
print y
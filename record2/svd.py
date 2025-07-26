# program 2: singular value decomposition using numpy

import numpy as np


A = np.array([[1,2,3], [4,5,6], [7, 8, 9]])
U, S, VT = np.linalg.svd(A)
print("Matrix A:\n",A)
n_comp = 2 
A_Reconstructed = np.dot(U[:,:n_comp], np.dot(np.diag(S[:n_comp]), VT[:n_comp, :]))
print("\nReconstructed matrix (with reduced dimension):\n",A_Reconstructed)
import numpy as np

A = np.loadtxt('pre-svd-big.txt')
A_k = np.loadtxt('rank-appx-big.txt')

num = np.linalg.norm((A - A_k), ord='fro')
denom = np.linalg.norm(A, ord='fro')

ratio = num/denom

print(ratio)


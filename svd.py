import numpy as np

A = np.loadtxt('m.txt', dtype=int)

# print(A)

U, first_D, V_t = np.linalg.svd(A)

# print("ShapeU: " + str(np.shape(U)) + " ShapeVt: " + str(np.shape(V_t)))

D = np.zeros((U.shape[1], V_t.shape[0]))
D[:first_D.size, :first_D.size] = np.diag(first_D)
# np.allclose

# print(" ")
# print(" ")
# print("MATRIX U:")
# print(U)
# print(" ")
# print(" ")
# print("MATRIX D:")
# print(newD)
# print(" ")
# print(" ")
# print("MATRIX V_t:")
# print(V_t)
# print(" ")
# print(" ")

# print(np.matmul(U, np.matmul(newD, V_t)))





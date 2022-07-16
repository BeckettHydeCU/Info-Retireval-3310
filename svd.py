import numpy as np

A = np.loadtxt('m_testpaper.txt', dtype=float)

print("Loaded matrix.")
# print(A)

U, first_D, V_t = np.linalg.svd(A)

print("Svd complete.")

print("ShapeU: " + str(np.shape(U)) + " ShapeVt: " + str(np.shape(V_t)))

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
# print(D)
# print(" ")
# print(" ")
# print("MATRIX V_t:")
# print(V_t)
# print(" ")
# print(" ")

# print(np.matmul(U, np.matmul(D, V_t)))

# print(" ")
# print(" ")

rank = 3

U = np.delete(U, slice(rank, U.shape[1]), axis=1)
D = np.delete(D, slice(rank, D.shape[1]), axis=1)
D = np.delete(D, slice(rank, D.shape[0]), axis=0)
V_t = np.delete(V_t, slice(rank, V_t.shape[0]), axis=0)

# print(U)

# print(" ")
# print(" ")

# print(D)

# print(" ")
# print(" ")

# print(V_t)

# print(" ")
# print(" ")


print("ShapeU: " + str(np.shape(U)) + " ShapeD: " + str(np.shape(D)) + "ShapeVt: " + str(np.shape(V_t)))

print("Rank appx:")
rankAppx = np.matmul(U, np.matmul(D, V_t))

print("Shape rankAppx: " + str(np.shape(rankAppx)))

print(rankAppx)

np.savetxt('rank-appx.txt', rankAppx)
np.savetxt('U-appx.txt', U)
np.savetxt('D-appx.txt', D)
np.savetxt('Vt-appx.txt', V_t)






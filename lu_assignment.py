import numpy as np

def doolittle(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    for i in range(n):
        # (Upper Triangular)
        for k in range(i, n):
            sum_up = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_up

        # (Lower Triangular)
        L[i][i] = 1  # Diagonal as 1
        for k in range(i+1, n):
            sum_up = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - sum_up) / U[i][i]
    return L, U

def lu_solve(L, U, b):
    n = len(b)
    # (Forward Substitution to solve Ly = b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - sum(L[i][j]*y[j] for j in range(i))

    # (Backward Substitution to solve Ux = y)
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(U[i][j]*x[j] for j in range(i+1, n))) / U[i][i]
    return x

A = np.array([
    [1, -1,  3,  2],
    [1,  5, -5, -2],
    [3, -5, 19,  3],
    [2, -2,  3, 21]
], dtype=float)
b = np.array([15, -35, 94, 1], dtype=float)
# Decompose A into L and U
L, U = doolittle(A)
# Solve the system using LU
x = lu_solve(L, U, b)
print(f"Result for vector x: {x}")
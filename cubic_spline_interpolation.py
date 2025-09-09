import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def my_cubic_spline_flat(x, y, X):
    n = len(x)
    if n < 2:
        raise ValueError("Needs a minimum of 2 data points")
    h = np.diff(x)
    A = np.zeros((n, n))
    B = np.zeros(n)
    A[0, 0] = 1.0
    A[n-1, n-1] = 1.0

    for i in range(1, n-1):
        A[i, i-1] = h[i-1]
        print(A)
        A[i, i] = 2.0 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        B[i] = 6.0 * ((y[i+1] - y[i])/ h[i] - (y[i] - y[i-1]) / h[i-1])

    S = np.linalg.solve(A, B)
    Y = np.zeros(len(X))

    for idx, xi in enumerate(X):
        if xi <= x[0]:
            i = 0
        elif xi >= x[-1]:
            i = n - 2
        else:
            i = np.searchsorted(x, xi) - 1
            if i >= n - 1:
                i = n - 2

        dx = xi - x[i]
        dx_interval = x[i+1] - x[i]

        a = y[i]
        b = (y[i+1] - y[i]) / dx_interval - dx_interval * (2*S[i] + S[i+1]) / 6.0
        c = S[i] / 2.0
        d = (S[i+1] - S[i]) / (6.0 * dx_interval)

        Y[idx] = a + b*dx + c*dx**2 + dx*dx**3
    return Y


x = np.array([0., 0.2, 0.4, 0.6, 0.8, 1., 1.2, 1.4, 1.6, 1.8, 2., 2.2, 2.4, 2.6, 2.8])
y = np.array([10., 11.216, 11.728, 11.632, 11.024, 10., 8.656, 7.088, 5.392, 3.664, 2., 0.496, -0.752, -1.648, -2.096])
X_test1 = np.array([0., 0.2, 0.4, 0.6, 0.8, 1., 1.2, 1.4, 1.6, 1.8, 2., 2.2, 2.4, 2.6, 2.7])
Y_test1 = my_cubic_spline_flat(x, y, X_test1)

print("Test 1 - Interpolation at original points:")
print("Original y values:")
print(y)
print("Interpolated Y values:")
print(Y_test1)
print("Max difference:", np.max(np.abs(y - Y_test1)))
print()


# Test 2
X_test2 = np.linspace(0, 2.8, 50)
Y_test2 = my_cubic_spline_flat(x, y, X_test2)

sns.set_context("poster")

plt.figure(figsize=(12, 8))
plt.scatter(x, y, color='b', s=100)
plt.plot(X_test2, Y_test2, 'y-', linewidth=2)
plt.scatter(X_test1, X_test1, color='r', s=50, zorder=4)
plt.title("Cubic Spline Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)
plt.show()


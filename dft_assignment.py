import time
import matplotlib.pyplot as plt
import numpy as np

start_time = time.time()
x = np.array([ 0.00000000e+00, 5.57590997e+00, 2.04087031e+00, -8.37717508e+00,
      -5.02028540e-01, 1.00000000e+01, -5.20431056e+00, -7.68722952e-01,
      -5.56758182e+00, 1.02781920e+01, 1.71450552e-15, -1.02781920e+01,
      5.56758182e+00, 7.68722952e-01, 5.20431056e+00, -1.00000000e+01,
      5.02028540e-01, 8.37717508e+00, -2.04087031e+00, -5.57590997e+00])

sr = 20
ts = 1/sr
n = len(x)
t = np.linspace(0, 1, n, endpoint=False)


def DFT(x):
      N = len(x)
      X = []
      for k in range(N):
            s = 0
            for n in range(N):
                  s += x[n]*np.exp(-2j*np.pi*k*n/N)
            X.append(s)
      return np.array(X)

X_dft = DFT(x)
freqs = np.fft.fftfreq(n, d=ts)

plt.figure(figsize=(12, 8))
plt.subplot(111)
plt.plot(t, x, "-b")
plt.plot(t, x, "ro")
plt.title("Sampled Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.tight_layout()
plt.show()

threshold = 1e-5
magnitude = np.abs(X_dft[:n//2])
significant_freqs = freqs[:n//2][magnitude > threshold]
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Estimated Frequencies of Physical Systems (Hz): {significant_freqs}")
print(f"Number of Physical Systems: {len(significant_freqs)}")
print(f"Elapsed time is: {elapsed_time:.5f}")
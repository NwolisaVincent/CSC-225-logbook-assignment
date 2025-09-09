import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
# let's deal with the sample rate and time vector

x = np.array([ 0.00000000e+00, 5.57590997e+00, 2.04087031e+00, -8.37717508e+00,
      -5.02028540e-01, 1.00000000e+01, -5.20431056e+00, -7.68722952e-01,
      -5.56758182e+00, 1.02781920e+01, 1.71450552e-15, -1.02781920e+01,
      5.56758182e+00, 7.68722952e-01, 5.20431056e+00, -1.00000000e+01,
      5.02028540e-01, 8.37717508e+00, -2.04087031e+00, -5.57590997e+00])

N = len(x)
t = np.linspace(0, 1, N, endpoint=False)
fs = 20
X_fft = np.fft.fft(x)
frequencies = np.fft.fftfreq(N, d=1 / fs)

X_mag = np.abs(X_fft)

half_N = N//2
frequencies_pos = frequencies[:half_N]
X_mag_pos = X_mag[:half_N]

end_time = time.time()
plt.figure(figsize=(12, 8))
plt.stem(frequencies_pos, X_mag_pos, basefmt="-r")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT of the Signal")
plt.grid(True)
plt.show()

threshold = 1e-5
magnitude = np.abs(X_fft[:N//2])
significant_freqs = frequencies_pos[:N//2][magnitude > threshold]
elapsed_time = end_time - start_time

print(f"Estimated Frequencies of Physical Systems (Hz): {significant_freqs}")
print(f"Number of Physical Systems: {len(significant_freqs)}")
print(f"Elapsed time is: {elapsed_time:.5f}")
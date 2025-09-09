# CSC-225-logbook-assignment (Python)
---
## This assignment includes the following:-
### - Cubic Spline Interpolation
### - Discrete Fourier Transform
### - Fast Fourier Transform
### - LU Decomposition
---
## <u>Definitions</u>:-
## Cubic Spline Interpolation:
#### This is a method of fitting a smooth curve through a set of given data points (x0, y0), (x1, y1),....,(xn, yn).
#### Instead of fitting one big polynomial (which can oscillate wildly), cubic splines use piecewise cubic polynomials between each pair of points.
## Advantages:
#### - Produces a smooth curve (continuous up to 2nd derivative).
#### - Avoids oscillations of high-degree polynomial interpolation.
#### - Very stable and widely used in graphics, numerical solutions, data fitting.
---
## Discrete Fourier Transform (DFT):
#### The DFT converts a finite sequence of complex (or real) time-domain samples x[n] (for n = 0,....N-1) into a sequence of complex frequency-domain samples X[k] (for k = 0,...,N-1). It tells you how much of each discrete frequency is present in the signal.
### DFT Formula: X[k] = Σ(n=0 to N-1) x[n] * e^(-j2πkn/N)
## Uses of DFT:-
#### - Spectral analysis (finding frequencies in signals)
#### - Filtering (design & implementation)
#### - Image processing (2D DFT / FFT)
#### - Digital communications (OFDM, modulation)
#### - Solving PDEs numerically (spectral methods)
#### - Audio processing (STFT uses windowed DFTs)
---
## Fast Fourier Transform (FFT):
#### FFT stands for Fast Fourier Transform, a crucial mathematical algorithm used to convert a time-domain signal into its frequency-domain components, revealing the signal's underlying frequencies and amplitudes. 
### FFT Formula: X[k] = Σ(n=0 to N-1) [x[n] * WN^kn]
## Uses of FFT:-
#### - Signal Processing
#### - Spectrum Analysis
#### - Audio Extraction
#### - Image Processing
---
## LU Decompostion:
#### LU decomposition is a method of factorizing a square matrix A into two matrices: A = LU
#### L = Lower triangular matrix (all zeros above diagonal, 1's on diagonal if we use Doolittle's method).
#### U = Upper triangular matrix (all zeros below the diagonal).
---
#### This is useful because it simplifies solving of equations Ax = b; instead of solving directly, you solve in two easier steps:
#### 1. Ly = b (forward substitution)
#### 2. Ux = y (backward substitution)
## Uses of LU Decomposition:
#### - Solving linear systems of equations (Ax = b)
#### - Calculating the matrix inverse
#### - Computing determinants
#### - Machine learning
#### - Scientific Computing and Simulation

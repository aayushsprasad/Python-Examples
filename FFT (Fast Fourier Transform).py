#FFT (Fast Fourier Transform)
#Name: Aayush Prasad @aprasad
import numpy as np

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    factor = np.exp(-2j * np.pi / N)
    return np.concatenate([even + factor**k * odd for k in range(N//2)])

signal = np.array([0, 1, 2, 3])
transformed_signal = fft(signal)
print("FFT of the signal:", transformed_signal)
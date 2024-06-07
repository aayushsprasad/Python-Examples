#Polynomial Regression
#Name: Aayush Prasad @aprasad
import numpy as np
from numpy.polynomial.polynomial import polyfit

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])

coefficients = polyfit(x, y, deg=2)
print("Polynomial coefficients:", coefficients)



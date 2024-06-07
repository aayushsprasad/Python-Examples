#Numerical Integration using Simpson's Rule
#Name: Aayush Prasad @aprasad
import numpy as np

def f(x):
    return x**2  # Example function

def simpsons_rule(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])

result = simpsons_rule(0, 1, 100)
print("Result of numerical integration:", result)
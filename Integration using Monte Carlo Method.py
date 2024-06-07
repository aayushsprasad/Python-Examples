#Integration using Monte Carlo Method
#Name: Aayush Prasad @aprasad
import numpy as np

def f(x):
    return x**2  # Example function

def monte_carlo_integration(a, b, n):
    random_x = np.random.uniform(a, b, n)
    return (b - a) * np.mean(f(random_x))

result = monte_carlo_integration(0, 1, 100000)
print("Result of Monte Carlo integration:", result)
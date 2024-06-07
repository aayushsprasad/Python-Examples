#Newton's Method for Finding Roots of Equations
##Name: Aayush Prasad @aprasad
def f(x):
    return x**3 - 2*x - 5  # Example function

def df(x):
    return 3*x**2 - 2  # Derivative of the function

def newton_method(x0, tolerance=1e-6, max_iterations=100):
    x = x0
    for _ in range(max_iterations):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Newton's method did not converge")

root = newton_method(2)
print("Approximate root found:", root)
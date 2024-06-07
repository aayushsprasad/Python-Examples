#Optimization using Gradient Descent
#Name: Aayush Prasad @aprasad
def f(x):
    return (x - 3)**2  # Example function

def gradient(x):
    return 2 * (x - 3)

def gradient_descent(x0, learning_rate=0.1, tolerance=1e-6, max_iterations=100):
    x = x0
    for _ in range(max_iterations):
        x_new = x - learning_rate * gradient(x)
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Gradient descent did not converge")

minimum = gradient_descent(0)
print("Minimum found by gradient descent:", minimum)
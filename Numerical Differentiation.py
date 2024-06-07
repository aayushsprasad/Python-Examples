#Numerical Differentiation
#Name: Aayush Prasad @aprasad
def f(x):
    return x**2  # Example function

def derivative(x, h=1e-6):
    return (f(x + h) - f(x)) / h

slope_at_point = derivative(2)
print("Slope at point x=2:", slope_at_point)
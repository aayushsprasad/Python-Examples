#Interpolation using Lagrange Polynomials
#Name: Aayush Prasad @aprasad
from sympy import symbols, simplify

def lagrange_interpolation(xs, ys):
    x = symbols('x')
    n = len(xs)
    result = 0
    for j in range(n):
        term = ys[j]
        for i in range(n):
            if i != j:
                term *= (x - xs[i]) / (xs[j] - xs[i])
        result += term
    return simplify(result)

xs = [0, 1, 2]
ys = [0, 1, 4]
polynomial = lagrange_interpolation(xs, ys)
print("Interpolating polynomial:", polynomial)

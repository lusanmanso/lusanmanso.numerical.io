# De forma analítica
import sympy as sp

x = sp.symbols('x')
f_sym = (1 - sp.cos(x)) / x**2
limit_sym = sp.limit(f_sym, x, 0)
print(limit_sym)

# De forma numérica
import numpy as np
if __name__ == "__main__":
   f = lambda x: (1-np.cos(x)) / x**2

   # Opcion de definir manual xi = [1.0e - 5, 1.0e - 6, 1.0e - 7, 1.0e - 8]
   xi = [1.0e-5 * 10 ** (-i) for i in range(7)]

   for x in xi:
      print(f"f({x}) = {f(x)}")

# Otro ej con error abs
fcc = lambda x: (1 - np.cos(x)) / x**2
xi = [10 ** (-i) for i in range(1, 12)]
for x in xi:
   print(f"f({x}) = {f(x)}")
   print(f"Error Absoluto:{abs(fcc(x) - f(x))}")
   print(f"Error Relativo:{abs(fcc(x) - f(x)) / f(x)}")

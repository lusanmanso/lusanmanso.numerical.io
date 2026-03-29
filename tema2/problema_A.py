# Problema A
# Implementar método de la secante en Python

import math

def secante(f, x1, x2, tol=1.e-6, maxit=100, verbose=True):
   for i in range(maxit):
      fx1 = f(x1)
      fx2 = f(x2)

      if abs(fx2 - fx1) < 1e-14:
         raise ZeroDivisionError(
            "Denom nearly 0"
         )

      x_new = x2 - fx2 * (x2 - x1) / (fx2 - fx1)

      if abs(x_new - x2) < tol:
         return x_new

      # actualizar valores para siguiente it
      x1, x2 = x2, x_new

   print("Max it reached")
   return x2

def f(x):
   return x * (math.exp(x/2) + 1)

if __name__ == "__main__":
   result = secante(f, 2.5, 2.0, 1.e-6, 50)
   print(result)

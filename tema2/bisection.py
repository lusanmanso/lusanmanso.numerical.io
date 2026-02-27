# Bisection method para encontrar raices de una función

def biseccion(f, a, b, tol=1.0e-6, maxit=200, verbose=False):
   fa, fb = f(a), f(b)
   assert fa * fb < 0, "No se cumplen las condiciones para aplicar M. Biseccion"

   for k in range(0, maxit):
      c = (a + b) / 2
      fc = f(c)

      if fa * fc < 0:
         b, fb = c, fc
      elif fc * fb < 0:
         a, fa = c, fc
      else:  # fc == 0
         break

      error = b - a
      if error < tol:
         break
   else:
      print(f"Numero maximo de iteraciones ({maxit}) alcanzado")

   return c

if __name__ == "__main__":
   from math import log

   f = lambda x: log(x) + x
   x_root = biseccion(f, 0.1, 1)
   print(f"x* = {x_root}")


import numpy as np
import scypy as sp

def f(x): return x**3 - 2
def df(x): return 3*(x**2)
def d2f(x): return 6*(x)

def halley(f, df, d2f, x0, x, tol=1.e-8, maxit=50, verbose=True):
   x_k = x0
   k = 0
   error = abs(x_k - x)

   while error > tol and k < maxit:
      x_next = x_k - ((2*f(x_k)*df(x_k)) / (2*(df(x_k)**2)-(f(x_k)*d2f(x_k))))
      error  = abs(x_next - x_k)

      k = k+1
      x_k = x_next # tenia que actualizar el punto :(

   return x_next

if __name__ == "__main__":

   x_aprox = halley(f, df, d2f, 1.3, 2**(1/3))

   e_k = abs(x_aprox - 1.3)
   # deberia de usar una form de r y C pero no
   print(f"Aprox Halley: {x_aprox}")
   print(f"Error e_k: {e_k}")

   # b) estudia si halley puede expresarse como it punto fijo
   """
   x_k+1 = g(x)
   """




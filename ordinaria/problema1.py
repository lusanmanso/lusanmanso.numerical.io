import numpy as np
import scypy as sp

# a) Implementa coef. binomial b = [a/2] para valores crecientes de a. Determina el mayor a para que la función devuelve resultado finito.

def fact(a):
   i = 1
   res = 1

   while (i <= a):
      # print(i)
      res = i*res
      i += 1

   res = float(res)
   return res

def binom_factorial(a):

   b = a // 2
   b = float(b)

   # res = (math.factorial(a)) / (math.factorial(b)*(math.factorial(a-b)))

   res = fact(a) / (fact(b)*fact(a-b))

   return res

if __name__ == "__main__":

   N = 172
   for i in range(N):
      print(f"It: {i}, Binom: {binom_factorial(i)}")

   """
   A partir del número 171 hay un error de representación en float, porque ya es demasiado grande.
   """

# b) Implementa producto y determina el mayor a) para el que devuelve resultado finito

def formula_producto(a, b):
   r = 1.0
   for i in range (1, b+1):
      r *= (a-b+i) / i
   return r

# c) Comprueba si ambas expresiones son equiv.

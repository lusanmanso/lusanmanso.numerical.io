import numpy as np
import sympy as sp

# a) reescribe de forma que evite cancelacion catastrofica implementa f_naive(x) original y f_estable(x) reescrita

def f_naive(x): return (1-sp.cos(x)) / (x**2)
def f_estable(x): return (sp.sin(x)**2) / (x**2*(1+sp.cos(x)))

# aproxima f''(0.004) con d. centrada para h: 10e-1 hasta e-8 usando ambas versiones de f

def f_segunda_naive(x, h):
   return (f_naive(x+h) -(2*f_naive(x)) + f_naive(x-h))/(h**2)

def f_segunda_estable(x, h):
   return (f_estable(x+h) - (2*f_estable(x)) + f_estable(x-h)) / (h**2)

# calcular

if __name__ == "__main__":
   print("Naive")
   print(f"It: 1\t Aprox: {f_segunda_naive(0.004, 10e-1)}")
   print(f"It: 2\t Aprox: {f_segunda_naive(0.004, 10e-2)}")
   print(f"It: 3\t Aprox: {f_segunda_naive(0.004, 10e-3)}")
   print(f"It: 4\t Aprox: {f_segunda_naive(0.004, 10e-4)}")
   print(f"It: 5\t Aprox: {f_segunda_naive(0.004, 10e-5)}")
   print(f"It: 6\t Aprox: {f_segunda_naive(0.004, 10e-6)}")
   print(f"It: 7\t Aprox: {f_segunda_naive(0.004, 10e-7)}")
   print(f"It: 8\t Aprox: {f_segunda_naive(0.004, 10e-8)}")

   print("Estable")
   print(f"It: 1\t Aprox: {f_segunda_estable(0.004, 10e-1)}")
   print(f"It: 2\t Aprox: {f_segunda_estable(0.004, 10e-2)}")
   print(f"It: 3\t Aprox: {f_segunda_estable(0.004, 10e-3)}")
   print(f"It: 4\t Aprox: {f_segunda_estable(0.004, 10e-4)}")
   print(f"It: 5\t Aprox: {f_segunda_estable(0.004, 10e-5)}")
   print(f"It: 6\t Aprox: {f_segunda_estable(0.004, 10e-6)}")
   print(f"It: 7\t Aprox: {f_segunda_estable(0.004, 10e-7)}")
   print(f"It: 8\t Aprox: {f_segunda_estable(0.004, 10e-8)}")

# c) Interpretar resultados
# debería de derivar f(x)
"""
Alrededor de la iteración 7 y 8. La d. naive comienza a oscilar enormemente, y eso se debe a que aunque lo óptimo sería reducir h lo máximo posible, este procedimiento ignora el error de redondeo (canc. catastrofica). La d. centrada al ser más precisa se puede permitir un h más grande antes de empezar a fallar.
"""

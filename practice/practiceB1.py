"""
Implementa el Método de Newton-Raphson para encontrar la raíz de f(x) = e^x - 3x^2 cerca de x = 1 usandolo. La tolerancia debe de ser de 10^-8
"""
# funcion recta tangente y=f(xk​)+f′(xk​)(x−xk​)
# metodo newton-raphson: xk+1​=xk​−f(xk​)/f′(xk​)

import math

# La fórmula de iteración de Newton-Raphson es:
#
#   x_{k+1} = x_k - f(x_k) / f'(x_k)
#
# Para f(x) = e^x - 3x^2, calculamos la derivada analítica:
#   f'(x) = e^x - 6x
#
# Sustituyendo, la fórmula de iteración ESPECÍFICA es:
#
#   x_{k+1} = x_k - (e^x_k - 3*x_k^2) / (e^x_k - 6*x_k)
#
# Punto de partida: x_0 = 1 (dado por el enunciado)
# Tolerancia: 1e-8

def f(x):
   return math.exp(x) - 3 * x**2

def df(x):
   return math.exp(x) - 6 * x

def newton_raphson(x0, tol=1e-8, max_iter=100):
   # x0 : aprox inicial
   # tol : tolerancia
   # max_iter : numero maximo de iteraciones para evitar bucles infinitos

   xk = x0
   for i in range(1, max_iter + 1):
       fxk = f(xk)
       dfxk = df(xk)

       # Evitar división por cero
       if dfxk == 0:
           print("Derivada es cero. No se puede continuar.")
           return None

       # nueva fortmula
       x_new = xk - fxk / dfxk

       print(f"Iter {i>3}: x = {x_new:.12f} | x_new - x_k | = {abs(x_new - xk):.3e}")

       # criterio de parada
       if abs(x_new  - xk) < tol:
          print(f"\n Convergencia alcanzada en {i} iteraciones.")
          return x_new, i

       xk = x_new

   # si se agotaron las iteraciones sin converger
   print("Max iter alcanzadas sin converger")
   return xk, max_iter

if __name__ == "__main__":
   x0 = 1.0
   root, n_iters = newton_raphson(x0, tol=1e-8)
   print(f"\nRaíz aproximada : {root:.12f}")
   print(f"f(raíz)         : {f(root):.6e}  ← debe ser ≈ 0")
   print(f"Iteraciones     : {n_iters}")

"""
El error se reduce drásticamente a cada paso. Esto es característico del método de Newton-Raphson, que tiene una convergencia cuadrática cerca de la raíz, lo que significa que el número de dígitos correctos se duplica aproximadamente en cada iteración.
"""

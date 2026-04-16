"""
Estima experimentalmente el orden de convergencia r del metodo implementado en el problema 1 usando el error absoluto entre aproximaciones sucesivas.

Toma como raíz exacta x* = 0.910007572488709$
¿Qué valor asintotico (C) se alcanza al fina
"""
# cuando converge un metodo iterativo los errores siguen un patrón matemativo
# que es el lim k -> inf (|ek+1| / |ek|^r) = C
# r: orden de convergencia
# C: constante asintótica

import math

# Newton-Raphson tiene ORDEN DE CONVERGENCIA r = 2 (cuadrático).
#
# Esto significa que los errores satisfacen:
#
#   lim_{k->inf}  |e_{k+1}| / |e_k|^2  =  C
#
# donde C es la constante asintótica de error, dada por:
#
#   C = |f''(x*)| / (2 * |f'(x*)|)
#
# Para f(x) = e^x - 3x^2:
#   f'(x)  = e^x - 6x      →  f'(x*) ≈ -2.9757
#   f''(x) = e^x - 6       →  f''(x*) ≈ -3.5157
#
#   C ≈ 3.5157 / (2 * 2.9757) ≈ 0.5907
#
# Si el experimento es correcto, el cociente debe estabilizarse
# cerca de 0.59 en las últimas iteraciones.

def f(x):
   return math.exp(x) - 3 * x**2

def df(x):
   return math.exp(x) - 6 * x

def newton_raphson(x0, tol=1e-8, max_iter=100):
   # x0 : aprox inicial
   # tol : tolerancia
   # max_iter : numero maximo de iteraciones para evitar bucles infinitos

   """
   Este necesita guardar todas las aprox x_k ne una lista para analizar la convergencia después
   """

   xk = x0
   history = [x0] # como primer elemento

   for i in range(1, max_iter + 1):
       fxk = f(xk)
       dfxk = df(xk)

       # Evitar división por cero
       if dfxk == 0:
           print("Derivada es cero. No se puede continuar.")
           return None

       # nueva fortmula
       x_new = xk - fxk / dfxk
       history.append(x_new) # guardar la nueva aproximación

       # print(f"Iter {i>3}: x = {x_new:.12f} | x_new - x_k | = {abs(x_new - xk):.3e}")

       # criterio de parada
       if abs(x_new  - xk) < tol:
          return history

       xk = x_new

   # si se agotaron las iteraciones sin converger
   return history

if __name__ == "__main__":

   x_exacta = 0.910007572488709 # dada por el enunciado
   x0 = 1.0
   history = newton_raphson(x0, tol=1e-8)

   # calcular errores absolutos
   errores = [abs(xk - x_exacta) for xk in history]

   # --- Imprimir tabla de resultados ---
   print("=" * 65)
   print(f"{'k':>4} | {'x_k':>20} | {'|e_k|':>12} | {'|e_{k+1}|/|e_k|^2':>18}")
   print("=" * 65)

   for k in range(len(errores)):
      xk = history[k]
      ek = errores[k]

      # El cociente solo existe desde k=0 si tenemos e_{k+1}
      if k < len(errores) - 1:
         ek1 = errores[k + 1]

         # Evitamos división por cero si el error ya es 0
         if ek == 0:
               cociente_str = "indefinido (e_k = 0)"
         else:
               cociente = ek1 / ek**2
               cociente_str = f"{cociente:>18.6f}"
      else:
         cociente_str = f"{'---':>18}"  # Última fila: no hay e_{k+1}

      print(f"{k:>4} | {xk:>20.12f} | {ek:>12.4e} | {cociente_str}")

   print("=" * 65)

   # --- Conclusión automática ---
   # Tomamos el cociente de la penúltima iteración (el más estable)
   if len(errores) >= 3 and errores[-3] != 0:
      C_experimental = errores[-2] / errores[-3]**2
      print(f"\nConstante C experimental (última iteración válida): {C_experimental:.6f}")
      print("Constante C teórica esperada: 0.590700")
      print(f"Diferencia relativa: {abs(C_experimental - 0.5907)/0.5907 * 100:.4f}%")

"""
El cociente se estabiliza cerca del 0.59 (confirmando que es r = 2). La constante C coincide con el valor experimental obtenido en las ultimas its
"""

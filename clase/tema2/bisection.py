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


"""
Biseccion
"""

# 1. IMPLEMENTACIÓN DE PUNTO FIJO
def punto_fijo(g, x0, tol, maxit):
    """
    g: Función de iteración (reorganización de f(x)=0 a x=g(x))
    x0: Semilla inicial o valor de partida
    tol: Tolerancia requerida (parada cuando |x_i - x_{i-1}| < tol)
    maxit: Máximo de iteraciones (seguridad por si diverge)
    """
    print("Iniciando algoritmo de Punto Fijo...")
    print("-" * 50)
    print(f"{'Iter':<5} | {'x_n':<15} | {'|x_n - x_n-1|':<15}")
    print("-" * 50)

    # Evaluar iterativamente la nueva aproximación: x_{i} = g(x_{i-1})
    x_prev = x0
    for i in range(1, maxit + 1):
        x_new = g(x_prev)

        # Calcular el residuo o error absoluto respecto a la iteración anterior
        error_abs = abs(x_new - x_prev)

        # Mostrar traza
        print(f"{i:<5} | {x_new:<15.6f} | {error_abs:<15.6e}")

        # CRITERIO DE PARADA (Condición de convergencia)
        if error_abs < tol:
            print("-" * 50)
            print(f"-> ¡Convergencia lograda en la iteración {i}!")
            return x_new, i

        # Actualizar memoria para siguiente vuelta
        x_prev = x_new

    print("-" * 50)
    print(f"-> ¡Alerta! Máximo número de iteraciones ({maxit}) alcanzado sin converger.")
    return x_new, maxit

# 2. TRANSFORMACIÓN: g(x) = 1 + 1/x
# Ojo, no dividir por cero. Asumimos x0 > 0.
def g_ej3(x):
    return 1.0 + (1.0 / x)

# 3. EJECUCIÓN
x0 = 1.0
tol_pf = 1e-4
maxit = 50

raiz_pf, iter_pf = punto_fijo(g_ej3, x0, tol_pf, maxit)

# 4. INTERPRETACIÓN GEOMÉTRICA (COBWEB / TELARAÑA)
# Dado g(x) = 1 + 1/x, su derivada es g'(x) = -1/x^2
# Al ser g'(1.618) ≈ -0.38 < 0, es un valor negativo pero menor de 1 en valor absoluto.
# La interpretación gráfica (Cobweb) muestra que en cada evaluación pasamos la
# función a la diagonal y=x, resultando en que la "telaraña" hace una ESPIRAL
# HASTA CONVERGER hacia adentro cruzando repetidamente el punto fijo.
# Si el g'(x)>0 (positivo) el dibujo iría aproximándose lentamente (o en escalera) de un lado.
print("\nRaíz encontrada con Punto Fijo:", round(raiz_pf, 6))
print("Nota geométrica: La convergencia es en ESPIRAL al ser g'(x) negativo (-1/x^2).")

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

# c) Interpretar resultados
# debería de derivar f(x)
"""
Alrededor de la iteración 7 y 8. La d. naive comienza a oscilar enormemente, y eso se debe a que aunque lo óptimo sería reducir h lo máximo posible, este procedimiento ignora el error de redondeo (canc. catastrofica). La d. centrada al ser más precisa se puede permitir un h más grande antes de empezar a fallar.
"""

if __name__ == "__main__":

    x0 = 0.004

    # valor exacto (analitico con sympy). OJO: hay que convertir 0.004 a racional
    # exacto (nsimplify) para no perder precision al construir el simbolo, si no
    # el "exacto" queda con un error del mismo orden que el que queremos medir.
    x = sp.symbols("x")
    expr = (1 - sp.cos(x)) / x**2
    d2 = sp.diff(expr, x, 2)
    exacto = float(d2.subs(x, sp.nsimplify(x0, rational=True)))

    # b) barrido h de 1e-1 a 1e-8 con ambas versiones de f

    hs = [10.0**(-i) for i in range(1, 9)]  # 1e-1, 1e-2, ..., 1e-8

    err_naive = [abs(f_segunda_naive(x0, h) - exacto) for h in hs]
    err_estable = [abs(f_segunda_estable(x0, h) - exacto) for h in hs]

    print(f"f''({x0}) exacto = {exacto:.9f}\n")
    print("Naive")
    for i, h in enumerate(hs, start=1):
        print(f"It: {i}\t h={h:.0e}\t Aprox: {f_segunda_naive(x0, h):.9f}\t Error: {err_naive[i-1]:.3e}")

    print("\nEstable")
    for i, h in enumerate(hs, start=1):
        print(f"It: {i}\t h={h:.0e}\t Aprox: {f_segunda_estable(x0, h):.9f}\t Error: {err_estable[i-1]:.3e}")

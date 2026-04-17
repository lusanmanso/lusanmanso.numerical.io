"""
Eq tiene 3 puntos fijos a < b < c
a = 0
b = (0,4, 0,4)
c = (2,6, 2,6)
"""

import math

def g(x):
    return (3 * x**2) / (1 + x**2)

def dg(x):
    return 6 * x / (1 + x**2) ** 2


def punto_fijo(g, x0, tol=1.0e-6, maxit=200, verbose=False):
    xk = x0

    if verbose:
        print("k\t\tx_k\t\tcota error")
        print(f"0\t\t{xk:.8f}\t")

    for k in range(1, maxit):
        xprev = xk
        xk = g(xprev)

        error = abs(xk - xprev)
        if verbose:
            print(f"{k}\t\t{xk:.8f}\t{error:e}")

        if error < tol:
            break
    else:
        xk = None
        print(f"Número máximo de iteraciones {maxit} alcanzado")

    return xk


def puntos_fijos():
    raiz1 = 0.0
    raiz2 = (3.0 - math.sqrt(5.0)) / 2.0
    raiz3 = (3.0 + math.sqrt(5.0)) / 2.0
    return [raiz1, raiz2, raiz3]

"""
pto fijo es repulsor si dg(x) > 1
pto fijo es atractor o repulsor dependiendo de dg superiores
"""
def clasificar_punto_fijo(x):
    derivada = abs(dg(x))
    if derivada < 1.0:
        return "atractor"
    if derivada > 1.0:
        return "repulsor"
    return "neutro"

def iterantes(g, x0, n=5):
    xk = x0
    valores = []
    for _ in range(n):
        xk = g(xk)
        valores.append(xk)
    return valores


if __name__ == "__main__":

    a, b, c = puntos_fijos()

    print("Puntos fijos:")
    for x in (a, b, c):
        print(f"x* = {x:.6f} | g'(x*) = {dg(x):.6f} | {clasificar_punto_fijo(x)}")

    print("Doms de atraccion:")
    print(f"0   : ({-b:.6f}, {b:.6f})")
    print(f"b   : solo x0 = {b:.6f}")
    print(f"c   : (-inf, {-b:.6f}) U ({b:.6f}, inf)")

    # convergencia a 0
    # desde el punto hasta -b
    # desde el punto a b
    casos = [
        ("Conv a 0", 0.2),
        ("Conv a c desde x0 < -b", -1.0),
        ("Conv a c desde x0 > b", 1.0),
    ]


    """
    for pt, x0 in casos:
        print(f"\n{pt}, x0 = {x0}")
        valores = iterantes(g, x0, n=5)
        for k, xk in enumerate(valores, start=1):
            print(f"x{k} = {xk:.10f}")
    """

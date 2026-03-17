"""
Usar aprox lineal: x_k = interseccion con el eje x de la recta que une (a, f(a)) y (b, f(b)) en lugar de punto medio
"""

def biseccion(f, a, b, tol=1.0e-6, maxit=20, verbose=False, aprox_lineal=True):
    fa, fb = f(a), f(b)
    assert fa * fb < 0, "No se cumplen condiciones para aplicar M. de Bisección"
    if verbose:
        print("k\t\tx_k\t\tcota error")

    if aprox_lineal:
        pendiente = (fb - fa) / (b - a) # eq de la pendiente
        # Pero no estoy declarando la recta bien
        recta = lambda x: (pendiente*a) + b # no es b
        c = recta(0)
        # interseccion con el eje x es valor de recta en
    else:
        c = (a+b) / 2

    for k in range(0, maxit):
        fc = f(c)
        if fa * fc < 0:
            b, fb = c, fc
        elif fc * fb < 0:
            a, fa = c, fc
        else:  # fc == 0
            if verbose:
                print(f"raíz exacta: x*: {c}")
            break

        error = b - a
        if verbose:
            print(f"{k}\t\t{c:.8f}\t{error:e}")

        if error < tol:
            break
    else:
        print(f"Número máximo de iteraciones {maxit} alcanzado")

    return c


if __name__ == "__main__":
    from math import cos

    f = lambda x: x - cos(x)
    eps = 1.0e-6

    """
    N = ceil((log(1 - 0.1) - log(2 * eps)) / log(2))
    print(
        f"Necesito calcular xk hasta k={N} para garantizar un error menor que eps={eps}"
    )
    """
    print("aprox_lineal=False: ")
    x_raiz = biseccion(f, -1, 1, tol=eps, verbose=False, aprox_lineal=False)
    print(f"x* = {x_raiz}")
    print(f"f(x*) = {f(x_raiz)}")
    print("aprox_lineal=True: ")
    x_raiz = biseccion(f, -1, 1, tol=eps, verbose=False, aprox_lineal=True)
    print(f"x* = {x_raiz}")
    print(f"f(x*) = {f(x_raiz)}")

    """
    --- OUTPUT ---
    aprox_lineal=False:
    x* = 0.0
    f(x*) = -1.0

    aprox_lineal=True:
    x* = 1.0
    f(x*) = 0.45969769413186023
    """

    # Se aprecia que con la aproximacion lineal el valor f(x*) es mucho mejor. Pero eso es declarando la recta mal

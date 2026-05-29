# Aproximar la serie de sumas parciales (problema de Basilea)
import math

def suma_basilea(N: int) -> float:
    if N < 1:
        raise ValueError("N debe ser >= 1")

    suma = 0.0
    for n in range(1, N + 1):
        suma += 1 / (n ** 2)
    return suma

if __name__ == "__main__":
    N = 10000  # cámbiarlo si se quiere
    sN = suma_basilea(N)
    valor_real = (math.pi ** 2) / 6
    error_abs = abs(sN - valor_real)

    print(f"N = {N}")
    print(f"S_N = {sN}")
    print(f"pi^2/6 = {valor_real}")
    print(f"Error absoluto = {error_abs}")

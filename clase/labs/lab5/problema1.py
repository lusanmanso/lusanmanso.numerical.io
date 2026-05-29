import math

class Dual:
    """Número dual a + b·d con d^2 = 0.

    Atributos:
        value : parte real, valor f(x).
        deriv : parte dual, valor f'(x).
    """

    def __init__(self, value, deriv):
        self.value = value
        self.deriv = deriv

    def __add__(self, other):
        return Dual(self.value + other.value, self.deriv + other.deriv)

    def __sub__(self, other):
        return Dual(self.value - other.value, self.deriv - other.deriv)


    def __mul__(self, other):
        return Dual(
            self.value * other.value,
            self.deriv * other.value + self.value * other.deriv,
        )

    def __truediv__(self, other):
        return Dual(
            self.value / other.value,
            (self.deriv * other.value - self.value * other.deriv) / other.value ** 2,
        )


def sin(d):
    return Dual(math.sin(d.value), d.deriv * math.cos(d.value))


def cos(d):
    return Dual(math.cos(d.value), -d.deriv * math.sin(d.value))


def exp(d):
    return Dual(math.exp(d.value), d.deriv * math.exp(d.value))


if __name__ == "__main__":
    # Para evaluar f'(x0) introducimos x = (x0, 1) y las constantes como (c, 0)
    x   = Dual(0.5, 1.0)   # variable independiente
    two = Dual(2.0, 0.0)   # constante 2

    result = exp(sin(two * x))

    print("=" * 45)
    print("Apartado (b)")
    print("=" * 45)
    print(f"Dual resultante : {result}")
    print(f"f(0.5)          = {result.value:.15f}")
    print(f"f'(0.5)  [AD]   = {result.deriv:.15f}")

    # (c) Derivada analitica y error absoluto
    # f(x) = e^sin(2x)  →  f'(x) = 2·cos(2x)·e^sin(2x)
    x0 = 0.5
    f_prime_exact = 2 * math.cos(2 * x0) * math.exp(math.sin(2 * x0))

    print()
    print("=" * 45)
    print("Apartado (c)")
    print("=" * 45)
    print(f"f'(0.5) [analítico] = {f_prime_exact:.15f}")
    print(f"Error absoluto      = {abs(result.deriv - f_prime_exact):.2e}")

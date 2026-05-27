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
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass


def sin(d):
    pass


def cos(d):
    pass


def exp(d):
    pass


if __name__ == "__main__":
    pass

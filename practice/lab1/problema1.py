from math import sqrt
import sympy as sp

"""
Considerar funcion dada. Escribir en python algo que evalue la funcion en potencias crecientes de 10 empezando en x = 10^4 hasta obtener error
"""

x = sp.symbols('x')
f = lambda x: 1 / (sqrt(x**2  + 1) - x)

"""
Buscar forma algebraicamente equivalente para escribir f(x) que evite la cancelacion catsatrofica. Evaluar para los mismos valores de x y calcualr el error absoluto y relativo cometido en el apartado a)
"""

fcc = lambda x: sqrt(x**2 + 1) / (x**2 + 1)**2 - x**2

if __name__ == "__main__":

   xi = [10 ** (i) for i in range(4, 8)]

   # Esto lo ejecute al principio

   for x in xi:
      print(f"f({x}) = {f(x)}")
      print(f"Error Absoluto:{abs(fcc(x) - f(x))}")
      print(f"Error Relativo:{abs(fcc(x) - f(x)) / f(x)}")
   

    # El error ha ocurrido en 10^8, porque una division de float en 0 ocurria. Es decir, el denominador se acercaba a valores tan cercanos al cero que habia cancelacion catastrofica

   for x in xi:
      print(f"fcc({x}) = {fcc(x)}")
      print(f"Error Absoluto:{abs(fcc(x) - f(x))}")
      print(f"Error Relativo:{abs(fcc(x) - f(x)) / f(x)}")

   # Reescribiendo la expresion a una similar aritmeticamente

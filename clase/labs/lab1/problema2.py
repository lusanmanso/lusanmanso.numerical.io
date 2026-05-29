import sympy as sp

x = 1234567891234567.0
y = 1234567891234566.0

"""
calcula x^2 - y^2 usando aritmatica de enteros (sin el .0)
este es resultado exacto porque python maneja enteros de precision arbitraria
"""

if __name__ == "__main__":

   flot = x**2 - y**2

   print(flot)

   id_not = x**2 - y**2
   fact = (x-y)*(x+y)


   print(id_not)
   print(fact)
   # Los prints no coinciden

   error = abs(fact - id_not)
   print(error)

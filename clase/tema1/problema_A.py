# Ecuación cuadrática con a = 1, b = 9^12 y c = -3
# Ocurre cancelación catastrófica al calcular x_+ cuando
# b > 0 y b^2  >> 4ac

from math import sqrt

def roots(a, b, c):
   sd = sqrt(b**2 - 4*a*c) # Raíz discriminante
   x1 = (-b + sd) / (2*a)
   x2 = (-b - sd) / (2*a)
   return x1, x2

# a, b, c = 1, 9**12, -3
a, b, c = 1, 10**8, 1

x1_cc, x2 = roots(a, b, c)
print(f"Raíz x1 con cancelación catastrófica: {x1_cc}")
print(f"Raíz x2 con cancelación catastrófica: {x2}")

x1 = c / (x2 * a)
print (f"Raíz x1 sin cancelación catastrófica: {x1:e}")

print(f"Error absoluto: {abs(x1 - x1_cc):e}")
print(f"Error relativo: {abs(x1 - x1_cc) / abs(x1):e}")

import math as m

"""
Implementa en Python las tres fórmulas de diferencias finitas vistas en clase
Aplicar para f(x) = xsin(x) para aproximar df(pi/2) cuyo valor exacto es = 1
"""

def f(x):
   return x * m.sin(x)

def f_der(x):
   return m.sin(x) + x*m.cos(x)

def calc_fd(f, x, h):
   # forwards difference
   return (f(x+h) - f(x)) / (h)

def calc_bd(f, x, h):
   return (f(x) - f(x-h)) / (h)

def calc_cd(f, x, h):
   return (f(x+h) - f(x-h)) / (2*h)

# Para cada formula calcula el error con 10^1, 10^-2, ..., 10^-4
"""
Comprueba experimentalmente que las no centradas son O(h) y las centradas es O(h^2)
"""
if __name__ == "__main__":
   x = m.pi / 2
   der_exacta = f_der(x)

   # print(der_exacta)

   hs = [10**(-i) for i in range (1, 5)]
   print("h\tprogresiva\tregresiva\tcentrada")
   for h in hs:
      fd = calc_fd(f, x, h)
      bd = calc_bd(f, x, h)
      cd = calc_cd(f, x, h)

      err_fd = abs(der_exacta - fd)
      err_bd = abs(der_exacta - bd)
      err_cd = abs(der_exacta - cd)

      # print(f"{h}\t{fd}\t{err_fd:e}")
      print(f"{h}\t{err_fd:e}\t{err_bd:e}\t{err_cd}")

"""
O(h): el error se divide por ~10 (linea recta en log-log)
O(h^2): el error se divide por ~100 (baja mucho más rapido)

En centradas, los terminos h se cancelan porque f(x+h) y f(x-h) son simétricos. Solo queda el termino en h^2 que es mucho mas pequeño cuando h es + pequeño.

En forward/backward no hay simetria asi que el primer error que queda es O(h)
En centradas CONVERGE 100 VECES MAS RAPIDO cuando divides h por 10
"""

import math as m

# implementa calc_5p
def f(x):
   return x * m.sin(x)

def f_der(x):
   return m.sin(x) + x*m.cos(x)

def calc_5p(f, x, h):
    return (f(x - 2*h) - 8*f(x-h) + 8*f(x+h)) - f(x-2*h)/ (h)

"""
aplicala a f = x*sin(x) para aproximar df(pi/2) cuyo valor exacto es 1
"""

if __name__ == "__main__":
   x = m.pi / 2
   der_exacta = f_der(x)

   hs = [10**(-i) for i in range (1, 6)]
   print("h\taprox\t\t\terror")
   for h in hs:

      five_p = calc_5p(f, x, h)

      err_five_p = abs(der_exacta - five_p)


      print(f"{h}\t{five_p}\t{err_five_p:e}")

"""
OUTPUT
h       aprox                   error
0.1     -10.499238319828125     1.149924e+01
0.01    -153.33813960886948     1.543381e+02
0.001   -1567.2083960220853     1.568208e+03
0.0001  -15704.390757534326     1.570539e+04
1e-05   -157076.06171174764     1.570771e+05

---

En dif. centradas, los terminos h se cancelan porque f(x+h) y f(x-h) son simétricos. Solo queda el termino en h^2 que es mucho mas pequeño cuando h es + pequeño.

En forward/backward, como es este caso, no hay simetria asi que el primer error que queda es O(h) (de ahí esa reducc de e+01, e+02, e+03 etc...)
"""


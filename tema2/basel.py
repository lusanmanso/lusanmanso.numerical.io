from math import pi
import numpy as np

f32 = np.float32

k = f32(1.0)
s = f32(0.0)

while True:
   termino = f32(1.0) / (k * k)
   s_new = s + termino
   if s_new == s:
      break
   s = s_new
   k += f32(1.0)

M = int(k) - 1
S_true = f32(pi) ** 2 / f32(6.0)

print(f"Ultima iteracion sumada M = {M}")
print(f"Ultimo termino sumado = {1.0 / (M * M):e}")
print(f"Suma S_M = {s}")
print(f"Error absoluto: {abs(s - S_true)}")
print(f"Error relativo: {abs(s - S_true) / abs(S_true)}")

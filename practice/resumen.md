
## Tema 1: Errores y Aritmética de Precisión Finita

- **Fuentes de Error:** En cálculo numérico, los errores provienen principalmente de la discretización (aproximar un problema continuo por uno discreto) y del redondeo (limitaciones de la aritmética del ordenador).

 - **Cuantificación del Error:** * El error absoluto mide la desviación directa: $|\Delta x| = |\tilde{x} - x|$.


   - El error relativo mide la desviación en proporción al tamaño real y es más útil para comparar magnitudes: $\delta x = \frac{\tilde{x} - x}{x}$.

- **Propagación y Cancelación Catastrófica:**
   - En sumas y restas se suman los errores absolutos, mientras que en multiplicaciones y divisiones se suman los errores relativos.
   - La cancelación catastrófica ocurre al restar números casi iguales ($a \approx b$), lo que hace que el denominador en la cota del error relativo sea muy pequeño, amplificando enormemente dicho error.
   - Para evitarla, se debe reformular algebraicamente la función.

* **Limitaciones de la Máquina:**
   * La precisión finita provoca falta de asociatividad: $(a+b)+c$ no siempre es igual a $a+(b+c)$ en el ordenador.
   * El Épsilon de la máquina (EPS) es el número positivo más pequeño tal que $1 + EPS \ne 1$.
   * Python utiliza por defecto precisión doble (64 bits) para los *floats*.
   * El *overflow* (desbordamiento) ocurre cuando el exponente supera el límite máximo representable, y el *underflow* (subdesbordamiento) cuando es tan pequeño que se aproxima a cero.

## Tema 2.1: Método de la Bisección

- **Fundamento Teórico:** Se basa en el Teorema de Bolzano, que establece que si $f(x)$ es continua en $[a,b]$ y hay un cambio de signo ($f(a) \cdot f(b) < 0$), existe al menos una raíz en ese intervalo. * **Iteración:** El método divide el intervalo a la mitad iterativamente calculando el punto medio $x_0 = \frac{a+b}{2}$. Se garantiza la convergencia siempre, aunque suele ser un proceso lento.

- **Criterios de Parada:** Es común detener el bucle cuando la diferencia entre iteraciones es menor a una tolerancia ($|x_k - x_{k-1}| < TOL$), cuando la función evaluada es muy cercana a cero ($|f(x_k)| < TOL_f$), o cuando la longitud del intervalo es suficientemente pequeña.

- **Convergencia y Estimación:** * Tiene convergencia lineal (orden $r=1$).
   * Puedes calcular el número de iteraciones máximas necesarias ($N$) para una tolerancia $\epsilon$ con la fórmula: $N = \lceil \frac{ln(b-a) - ln(2\epsilon)}{ln(2)} \rceil$.

## Tema 2.2: Iteración de Punto Fijo (Hasta Interp. Geométrica)

- **Concepto:** Se busca un punto $x^*$ tal que $g(x^*) = x^*$. Para hallar las raíces de $f(x) = 0$, se transforma algebraicamente la ecuación a la forma $x = g(x)$.

- **Proceso Iterativo:** Partiendo de un punto inicial $x_0$, se genera una secuencia evaluando $x_{k+1} = g(x_k)$.

- **Interpretación Geométrica:** Gráficamente, el método encuentra la intersección entre la recta $y = x$ y la curva $y = g(x)$. Al iterar, se traza un camino en forma de "escalera" o "telaraña" alternando movimientos verticales (evaluar la función) y horizontales (reflejar en $y=x$).

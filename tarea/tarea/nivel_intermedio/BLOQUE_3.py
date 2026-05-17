from core import Screen


class Bloque_3:

    # ==================================================
    # PREGUNTA 1
    # ==================================================

    def b3question_1(self):

        Screen.limpiar()

        Screen.titulo(
            "PREGUNTA 1"
        )

        print("""
1. Con a=20 y b=4 imprime todos los operadores aritméticos y sus resultados.

    a = 20
    b = 4
        """)

        a = 20
        b = 4

        print("\nRESPUESTA:\n")

        print(f"Suma            -> {a} + {b} = {a + b}")

        print(f"Resta           -> {a} - {b} = {a - b}")

        print(f"Multiplicacion  -> {a} * {b} = {a * b}")

        print(f"Division        -> {a} / {b} = {a / b}")

        print(f"Modulo          -> {a} % {b} = {a % b}")

        print(f"Potencia        -> {a} ** {b} = {a ** b}")

        print(f"Division Entera -> {a} // {b} = {a // b}")

        Screen.pausa()

    # ==================================================
    # PREGUNTA 2
    # ==================================================

    def b3question_2(self):

        Screen.limpiar()

        Screen.titulo(
            "PREGUNTA 2"
        )

        print("""
2. Crea dos listas idénticas y demuestra que "==" es True pero "is" es False.
        """)

        a = [1, 2]
        b = [1, 2]

        print("\nRESPUESTA:\n")

        print(f"Lista a -> {a}")

        print(f"Lista b -> {b}")

        print(f"\na == b -> {a == b}")

        print(f"a is b -> {a is b}")

        print("""

EXPLICACION:

== : compara los valores.

is : compara si ambas variables son el mismo objeto en memoria.
        """)

        Screen.pausa()

    # ==================================================
    # PREGUNTA 3
    # ==================================================

    def b3question_3(self):

        Screen.limpiar()

        Screen.titulo(
            "PREGUNTA 3"
        )

        print("""
3. Evalúa la siguiente expresión: x = 2 + 1 * 2 % 2 + (2**1)//2
        """)

        x = 2 + 1 * 2 % 2 + (2**1)//2

        print("\nRESPUESTA:\n")

        print(f"Resultado final -> {x}")

        print("""

ORDEN DE EVALUACION:

1. Potencia
   2**1 = 2

2. Multiplicacion
   1*2 = 2

3. Modulo
   2%2 = 0

4. Division Entera
   2//2 = 1

5. Suma Final
   2 + 0 + 1 = 3
        """)

        Screen.pausa()
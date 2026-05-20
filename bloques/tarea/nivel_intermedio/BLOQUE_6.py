from core import Screen

class Bloque_6():
    # ==================================================
    # PREGUNTA 1
    # ==================================================

    def b6question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Imprime los numeros del 1 al 10 usando while.
    """)

        # ==================================================
        # PROCESO
        # ==================================================

        number = 1

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar("""

                NUMEROS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        while number <= 10:

            print(f"Numero : {number}")

            number += 1

        Screen.mostrar("""
    """)

        Screen.pausa()

# ==================================================
# PREGUNTA 2
# ==================================================

    def b6question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Recorre una lista de frutas usando enumerate().
    """)

        # ==================================================
        # LISTA
        # ==================================================

        fruits = ["Manzana", "Banana", "Pera", "Uva", "Sandia"]

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")
        print(f"Lista: {fruits}")

        Screen.mostrar("""

                FRUTAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        for index, fruit in enumerate(fruits):

            print(f"Indice {index} -> {fruit}")

        Screen.mostrar("""

    """)

        Screen.pausa()

    # ==================================================
    # PREGUNTA 3
    # ==================================================

    def b6question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Crear lista de cuadrados de pares del 1 al 10 usando list comprehension.
    """)

        # ==================================================
        # LIST COMPREHENSION
        # ==================================================

        squares = [number**2 for number in range(1, 11) if number % 2 == 0]

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar("""

                RESULTADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        print(f"Lista : {squares}")

        Screen.mostrar("""

    """)

        Screen.pausa()

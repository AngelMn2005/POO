from core import Screen
class Bloque_9():

# ==================================================
# PREGUNTA 1
# ==================================================

    def b9question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Crear una tupla con 4 elementos e intentar modificar el primero.
    """)

        # ==================================================
        # TUPLA
        # ==================================================

        numbers = (10, 20, 30, 40)

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Tupla original : {numbers}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        print("""
    ERROR:

    Las tuplas son inmutables.
    No se pueden modificar despues de ser creadas.

    Ejemplo:

    numbers[0] = 99

    Resultado:

    TypeError
    """)

        Screen.pausa()


# ==================================================
# PREGUNTA 2
# ==================================================

    def b9question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Usar unpacking para asignar valores de una tupla.
    """)

        # ==================================================
        # TUPLA
        # ==================================================

        values = (100, 200, 300, 400)

        # ==================================================
        # UNPACKING
        # ==================================================

        a, b, *rest = values

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Tupla  : {values}

    a      : {a}

    b      : {b}

    resto  : {rest}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()


# ==================================================
# PREGUNTA 3
# ==================================================

    def b9question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Recorrer coordenadas usando for.
    """)

        # ==================================================
        # LISTA DE TUPLAS
        # ==================================================

        coordinates = [(10, 20), (30, 40), (50, 60)]

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                COORDENADAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Lista : {coordinates}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        for x, y in coordinates:

            print(f"x = {x} | y = {y}")

        print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()

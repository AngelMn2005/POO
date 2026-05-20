from core import Screen

class Bloque_11():
    # ==================================================
    # PREGUNTA 1
    # ==================================================

    def b11question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Crear dos conjuntos y calcular: union, interseccion y diferencia.
    """)

        # ==================================================
        # CONJUNTOS
        # ==================================================

        A = {1, 2, 3, 4}

        B = {3, 4, 5, 6}

        # ==================================================
        # OPERACIONES
        # ==================================================

        union = A | B

        intersection = A & B

        difference = A - B

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(f"""

                CONJUNTOS
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    A               : {A}

    B               : {B}

    Union           : {union}

    Interseccion    : {intersection}

    Diferencia      : {difference}


    """)

        Screen.pausa()


    # ==================================================
    # PREGUNTA 2
    # ==================================================

    def b11question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Eliminar duplicados usando set.
    """)

        # ==================================================
        # LISTA
        # ==================================================

        numbers = [1, 2, 2, 3, 3, 3, 4]

        # ==================================================
        # ELIMINAR DUPLICADOS
        # ==================================================

        result = list(set(numbers))

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(f"""

                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Lista original  : {numbers}

    Sin duplicados  : {result}


    """)

        Screen.pausa()


    # ==================================================
    # PREGUNTA 3
    # ==================================================

    def b11question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Calcular: (A | B) - (A & B)
    """)

        # ==================================================
        # CONJUNTOS
        # ==================================================

        A = {1, 2, 3, 4}

        B = {3, 4, 5, 6}

        # ==================================================
        # OPERACION
        # ==================================================

        result = (A | B) - (A & B)

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(f"""

                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    A           : {A}

    B           : {B}

    Resultado   : {result}


    """)

        print("""
    EXPLICACION:

    (A | B): Union de ambos conjuntos.

    (A & B): Elementos compartidos.

    Resultado:
    Elementos que NO comparten.

    Esto se conoce como: Diferencia simetrica.
    """)

        Screen.pausa()
from core import Screen,iniciar, positivo ,log
class Bloque_13():
# ==================================================
# PREGUNTA 1
# ==================================================

    def b13question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Crea un decorador que imprima
    "Iniciando..." antes de ejecutar la función.
    """)

        # ==================================================
        # FUNCION
        # ==================================================

        @iniciar
        def saludo():

            print("Hola mundo")

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        saludo()

        Screen.pausa()
# ==================================================
# PREGUNTA 2
# ==================================================

    def b13question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Decorador que verifique que el numero sea positivo antes de calcular su cuadrado.
    """)

        # ==================================================
        # FUNCION
        # ==================================================

        @positivo
        def cuadrado(number):

            return number ** 2

        # ==================================================
        # INGRESAR NUMERO
        # ==================================================

        while True:

            try:

                number = int(input("\nIngrese un numero: "))

                result = cuadrado(number)

                # SI ES NEGATIVO
                if result is None:

                    continue

                break

            except ValueError:

                Screen.error("Debe ingresar un numero entero.")

        # ==================================================
        # RESPUESTA
        # ==================================================
        Screen.limpiar()
        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Numero     : {number}

    Cuadrado   : {result}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()
# ==================================================
# PREGUNTA 3
# ==================================================

    def b13question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Analiza:
    @log
    def suma(a,b)
    ¿Que imprime suma(2,3)?
    """)

        # ==================================================
        # FUNCION
        # ==================================================

        @log
        def suma(a, b):

            return a + b

        # ==================================================
        # RESULTADO
        # ==================================================

        result = suma(2, 3)

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Resultado : {result}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()
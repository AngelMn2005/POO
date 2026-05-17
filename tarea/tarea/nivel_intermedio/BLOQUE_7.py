from core import Screen, ValidationMixin


class Bloque_7(ValidationMixin):

    # ==================================================
    # PREGUNTA 1
    # ==================================================

    def b7question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Funcion que calcule el doble de un numero.
    """)

        # ==================================================
        # FUNCION
        # ==================================================

        def doble(x):

            return x * 2

        # ==================================================
        # ETIQUETA
        # ==================================================

        Screen.gotoxy(3, 8)
        print("=== INGRESAR DATO ===")

        Screen.gotoxy(1, 10)
        print("Numero:")

        # ==================================================
        # NUMERO
        # ==================================================

        while True:

            # LIMPIAR ERROR
            Screen.gotoxy(1, 13)
            print(" " * 100, end="")

            # LIMPIAR INPUT
            Screen.gotoxy(10, 10)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(10, 10)

            number = input().strip()

            # VALIDAR VACIO
            if not self.validar_vacio(number):

                Screen.gotoxy(1, 12)

                Screen.error("El numero no puede estar vacío.")

                continue

            # VALIDAR NUMERO
            try:

                number = float(number)

            except ValueError:

                Screen.gotoxy(1, 12)

                Screen.error("El numero debe ser numerico.     ")

                continue

            break

        # ==================================================
        # PROCESO
        # ==================================================

        result = doble(number)

        Screen.limpiar()

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Numero ingresado : {number}
    Doble            : {result}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()

    # ==================================================
    # PREGUNTA 2
    # ==================================================

    def b7question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Funcion que sume elementos usando *args.
    """)

        # ==================================================
        # FUNCION
        # ==================================================

        def sum_numbers(*args):

            return sum(args)

        # ==================================================
        # LISTA
        # ==================================================

        numbers = [10, 20, 30, 40]

        # ==================================================
        # PROCESO
        # ==================================================

        result = sum_numbers(*numbers)

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Lista       : {numbers}
    Suma total  : {result}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()

    # ==================================================
    # PREGUNTA 3
    # ==================================================

    def b7question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Funcion recursiva para calcular el factorial.
    """)

        # ==================================================
        # FUNCION
        # ==================================================

        def factorial(n):

            if n == 0 or n == 1:

                return 1

            return n * factorial(n - 1)

        # ==================================================
        # ETIQUETA
        # ==================================================

        Screen.gotoxy(3, 8)
        print("=== INGRESAR DATO ===")

        Screen.gotoxy(1, 10)
        print("Numero:")

        # ==================================================
        # NUMERO
        # ==================================================

        while True:

            # LIMPIAR ERROR
            Screen.gotoxy(1, 13)
            print(" " * 100, end="")

            # LIMPIAR INPUT
            Screen.gotoxy(10, 10)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(10, 10)

            number = input().strip()

            # VALIDAR VACIO
            if not self.validar_vacio(number):

                Screen.gotoxy(1, 12)

                Screen.error("El numero no puede estar vacío.")

                continue

            # VALIDAR DECIMAL
            if "." in number or "," in number:

                Screen.gotoxy(1, 12)

                Screen.error("No se permiten numeros decimales.")

                continue

            # VALIDAR NUMERO
            try:

                number = int(number)

            except ValueError:

                Screen.gotoxy(1, 12)

                Screen.error("El numero debe ser numerico.")

                continue

            # VALIDAR NEGATIVO
            if number < 0:

                Screen.gotoxy(1, 12)

                Screen.error("El numero no puede ser negativo.")

                continue

            break

        # ==================================================
        # VALIDAR LIMITE
        # ==================================================

        if number > 50:

            Screen.gotoxy(1, 12)

            Screen.error("El numero es demasiado grande.")

            Screen.pausa()

            return

        # ==================================================
        # PROCESO
        # ==================================================

        result = factorial(number)

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Numero    : {number}
    Factorial : {result}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()
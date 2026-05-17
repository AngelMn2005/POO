from core import Screen, ValidationMixin

class Bloque_12(ValidationMixin):
    # ==================================================
    # PREGUNTA 1
    # ==================================================

    def b12question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Captura el ValueError al convertir input del usuario a int.
    """)

        # ==================================================
        # INGRESAR NUMERO
        # ==================================================
        Screen.gotoxy(3, 8)
        print("=== INGRESAR DATO ===")

        Screen.gotoxy(1, 10)
        print("Ingrese un numero: ")                
        
        while True:

            # LIMPIAR ERROR
            Screen.gotoxy(1, 12)
            print(" " * 100, end="")

            # LIMPIAR INPUT
            Screen.gotoxy(22, 10)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(22, 10)

            number = input().strip()

            # VALIDAR VACIO
            if not self.validar_vacio(number):

                Screen.gotoxy(1, 13)

                Screen.error("El campo no puede estar vacío.    ")

                continue

            # VALIDAR ENTERO
            try:

                number = int(number)

                break

            except ValueError:

                Screen.gotoxy(1, 13)

                Screen.error("Debe ingresar solo numeros enteros.")
        Screen.limpiar()
        # ==================================================
        # RESPUESTA
        # ==================================================

        print(f"""

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Numero ingresado : {number}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()
        
    # ==================================================
    # PREGUNTA 2
    # ==================================================

    def b12question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Captura IndexError al acceder una posicion invalida de una lista.
    """)

        # ==================================================
        # LISTA
        # ==================================================

        numbers = [10, 20, 30]

        print(f"\nLista: {numbers}")
            # ETIQUETA
        Screen.gotoxy(1, 11)
        print("Ingrese posicion: ")
        # ==================================================
        # INGRESAR POSICION
        # ==================================================

        while True:

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 100, end="")
            # LIMPIAR INPUT
            Screen.gotoxy(21, 11)
            print(" " * 30, end="")
            
            # POSICION CURSOR
            Screen.gotoxy(21, 11)

            position = input().strip()

            # VALIDAR VACIO
            if not self.validar_vacio(position):

                Screen.gotoxy(1, 13)

                Screen.error("La posicion no puede estar vacia.")

                continue

            # VALIDAR NUMERO
            try:

                position = int(position)

            except ValueError:

                Screen.gotoxy(1, 13)

                Screen.error("Debe ingresar un numero entero.  ")

                continue

            # ==================================================
            # CAPTURAR INDEXERROR
            # ==================================================

            try:

                value = numbers[position]

                break

            except IndexError:

                Screen.gotoxy(1, 13)

                Screen.error("La posicion no existe en la lista.")

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Lista      : {numbers}

    Posicion   : {position}

    Valor      : {value}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()
    
    # ==================================================
    # PREGUNTA 3
    # ==================================================

    def b12question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Manejar ValueError y ZeroDivisionError.
    """)

        # ==================================================
        # NUMERO 1
        # ==================================================

        while True:

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 100, end="")

            # ETIQUETA
            Screen.gotoxy(1, 7)
            print("Ingrese numero 1: ")

            # LIMPIAR INPUT
            Screen.gotoxy(19, 7)
            print(" " * 100, end="")

            # POSICION CURSOR
            Screen.gotoxy(19, 7)

            num1 = input().strip()

            # VALIDAR VACIO
            if not self.validar_vacio(num1):

                Screen.gotoxy(1, 13)

                Screen.error("El numero 1 no puede estar vacío.")

                continue

            # VALIDAR NUMERO
            try:

                num1 = int(num1)

                break

            except ValueError:

                Screen.gotoxy(1, 13)

                Screen.error("El numero 1 debe ser entero.        ")

        # ==================================================
        # NUMERO 2
        # ==================================================
            # ETIQUETA
        Screen.gotoxy(1, 9)
        print("Ingrese numero 2: ")
        while True:

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 100, end="")

            # LIMPIAR INPUT
            Screen.gotoxy(19, 9)
            print(" " * 100, end="")

            # POSICION CURSOR
            Screen.gotoxy(19, 9)

            num2 = input().strip()

            # VALIDAR VACIO
            if not self.validar_vacio(num2):

                Screen.gotoxy(1, 13)

                Screen.error("El numero 2 no puede estar vacío.       ")

                continue

            # VALIDAR NUMERO
            try:

                num2 = int(num2)

                # ==================================================
                # TRY DIVISION
                # ==================================================

                try:

                    result = num1 / num2

                    break

                except ZeroDivisionError:

                    Screen.gotoxy(1, 13)

                    Screen.error("No se puede dividir para cero.        ")

            except ValueError:

                Screen.gotoxy(1, 13)

                Screen.error("El numero 2 debe ser entero.       ")

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Numero 1   : {num1}

    Numero 2   : {num2}

    Division   : {result}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()
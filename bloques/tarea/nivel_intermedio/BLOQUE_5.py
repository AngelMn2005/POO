from core import Screen, ValidationMixin, ask_continuar

class Bloque_5(ValidationMixin):
    # ==================================================
    # PREGUNTA 1
    # ==================================================

    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def b5question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Programa que determine si un numero es par o impar.
    """)

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

            # LIMPIAR INPUT
            Screen.gotoxy(10, 10)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(10, 10)

            number = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 12)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(number):

                Screen.gotoxy(1, 12)

                Screen.error("El numero no puede estar vacío.               ")

                continue

            # VALIDAR DECIMALES
            if "." in number or "," in number:

                Screen.gotoxy(1, 12)

                Screen.error("No se permiten numeros decimales.                 ")

                continue

            # VALIDAR NUMERO
            try:

                number = int(number)

            except ValueError:

                Screen.gotoxy(1, 12)

                Screen.error("El numero debe ser numerico.                       ")

                continue

            break

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        Screen.aviso("\nRESPUESTA:\n")

        if number % 2 == 0:

            Screen.mostrar(f"""

                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    {number} es un numero PAR.


    """)

        else:

            Screen.mostrar(f"""

                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    {number} es un numero IMPAR.


    """)


# ==================================================
# PREGUNTA 2
# ==================================================

    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def b5question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Asigna una calificacion letra segun nota numerica.
    """)

        # ==================================================
        # ETIQUETA
        # ==================================================

        Screen.gotoxy(3, 8)
        print("=== INGRESAR DATO ===")

        Screen.gotoxy(1, 10)
        print("Nota:")

        # ==================================================
        # NOTA
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(10, 10)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(10, 10)

            grade = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 12)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(grade):

                Screen.gotoxy(1, 12)

                Screen.error("La nota no puede estar vacía.                          ")

                continue

            # VALIDAR NUMERO
            try:

                grade = float(grade)

            except ValueError:

                Screen.gotoxy(1, 12)

                Screen.error("La nota debe ser numerica.                                    ")

                continue

            # VALIDAR RANGO
            if grade < 0 or grade > 100:

                Screen.gotoxy(1, 12)

                Screen.error("La nota debe estar entre 0 y 100.                                     ")

                continue

            break

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        Screen.aviso("\nRESPUESTA:\n")

        if grade >= 90:

            result = "A"

        elif grade >= 80:

            result = "B"

        elif grade >= 70:

            result = "C"

        else:

            result = "D"

        Screen.mostrar(f"""

                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Nota          : {grade}
    Calificacion  : {result}


    """)


# ==================================================
# PREGUNTA 3
# ==================================================

    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def b5question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Sistema de login.
    """)

        # ==================================================
        # ETIQUETAS
        # ==================================================

        Screen.gotoxy(3, 8)
        print("=== INGRESAR DATOS ===")

        Screen.gotoxy(1, 10)
        print("Usuario:")

        Screen.gotoxy(1, 12)
        print("Password:")

        # ==================================================
        # USUARIO
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(11, 10)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(11, 10)

            user = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(user):

                Screen.gotoxy(1, 14)

                Screen.error("El usuario no puede estar vacío.                                  ")

                continue

            break

        # ==================================================
        # PASSWORD
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(11, 12)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(11, 12)

            password = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(password):

                Screen.gotoxy(1, 14)

                Screen.error("La password no puede estar vacía.                                 ")

                continue

            break
        Screen.limpiar()

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")

        if user == "admin" and password == "123":

            Screen.mostrar("""

                    LOGIN
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Bienvenido Admin.


    """)

        else:

            Screen.mostrar("""

                    LOGIN
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Acceso denegado.

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)


from core import Screen, ValidationMixin, ask_continuar

class Bloque_4(ValidationMixin,Screen):
    # ==================================================
    # PREGUNTA 1
    # ==================================================

    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def b4question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Solicita nombre y edad; muestra un mensaje personalizado con f-string.
    """)

        # ==================================================
        # ETIQUETAS
        # ==================================================
        Screen.gotoxy(3, 8)
        print("===INGRESAR DATOS====")
        Screen.gotoxy(1, 10)
        print("Nombre:")

        Screen.gotoxy(1, 12)
        print("Edad:")

        # ==================================================
        # NOMBRE
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(10, 10)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(10, 10)

            name = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(name):

                Screen.gotoxy(1, 14)

                self.error("El nombre no puede estar vacío.             ")

                continue

            # VALIDAR SOLO LETRAS
            if not self.validar_solo_letras(name):

                Screen.gotoxy(1, 14)

                self.error("El nombre solo debe contener letras.        ")

                continue

            # NORMALIZAR
            name = self.normalizar_texto(name)

            break

        # ==================================================
        # EDAD
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(10, 12)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(10, 12)

            age = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(age):

                Screen.gotoxy(1, 14)

                self.error("La edad no puede estar vacía.           ")

                continue

            # VALIDAR NUMERO
            try:

                age = int(age)

            except ValueError:

                Screen.gotoxy(1, 14)

                self.error("La edad debe ser numerica.                  ")

                continue

            # VALIDAR EDAD
            if age <= 0:

                Screen.gotoxy(1, 14)

                self.error("La edad debe ser mayor a 0.                     ")

                continue
            break
        Screen.limpiar()
        Screen.aviso("\nRESPUESTA:\n")
        Screen.mostrar(f"""

                INFORMACION

    Nombre : {name}
    Edad   : {age}

    """)
    # ==================================================
    # PREGUNTA 2
    # ==================================================

    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def b4question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Lee dos números, calcula su suma y promedio.
    """)

        # ==================================================
        # ETIQUETAS
        # ==================================================

        Screen.gotoxy(3, 8)
        print("=== INGRESAR DATOS ===")

        Screen.gotoxy(1, 10)
        print("Numero 1:")

        Screen.gotoxy(1, 12)
        print("Numero 2:")

        # ==================================================
        # NUMERO 1
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(12, 10)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(12, 10)

            num1 = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(num1):

                Screen.gotoxy(1, 14)

                self.error("El numero 1 no puede estar vacío.               ")

                continue

            # VALIDAR NUMERO
            try:

                num1 = float(num1)

            except ValueError:

                Screen.gotoxy(1, 14)

                self.error("El numero 1 debe ser numerico.                  ")

                continue

            break

        # ==================================================
        # NUMERO 2
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(12, 12)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(12, 12)

            num2 = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(num2):

                Screen.gotoxy(1, 14)

                self.error("El numero 2 no puede estar vacío.                       ")

                continue

            # VALIDAR NUMERO
            try:

                num2 = float(num2)

            except ValueError:

                Screen.gotoxy(1, 14)

                self.error("El numero 2 debe ser numerico.                              ")

                continue

            break

        # ==================================================
        # OPERACIONES
        # ==================================================

        suma = num1 + num2

        promedio = suma / 2

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(f"""

                RESULTADOS

    Numero 1 : {num1}
    Numero 2 : {num2}

    Suma     : {suma}
    Promedio : {promedio}

    """)

# ==================================================
# PREGUNTA 3
# ==================================================

    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def b4question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Sin convertir el input, imprime numero + "5".
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

                self.error("El numero no puede estar vacío.                         ")

                continue

            break

        # ==================================================
        # OPERACION
        # ==================================================

        result = number + "5"

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(f"""

                RESULTADO

    Numero ingresado : {number}
    Resultado        : {result}

    """)

        print("""
    EXPLICACION:

    Como input devuelve texto, Python concatena strings.

    Ejemplo:
    "10" + "5" = "105"
    "Hola" + "5" = "Hola5 "
    """)


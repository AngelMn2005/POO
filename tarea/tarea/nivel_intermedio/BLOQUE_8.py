from core import Screen, ValidationMixin

class Bloque_8(ValidationMixin):
    # ==================================================
    # PREGUNTA 1
    # ==================================================

    def b8question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Crear una lista, agregar 3 elementos con append(), ordenarla y mostrarla.
    """)

        # ==================================================
        # LISTA
        # ==================================================

        numbers = []

        # ==================================================
        # ETIQUETAS
        # ==================================================

        Screen.gotoxy(3, 8)
        print("=== INGRESAR DATOS ===")

        # ==================================================
        # INGRESAR NUMEROS
        # ==================================================

        for i in range(3):

            while True:

                # LIMPIAR ERROR
                Screen.gotoxy(1, 16)
                print(" " * 100, end="")

                # ETIQUETA
                Screen.gotoxy(1, 10 + (i * 2))
                print(f"Numero {i + 1}:")

                # LIMPIAR INPUT
                Screen.gotoxy(12, 10 + (i * 2))
                print(" " * 30, end="")

                # POSICION CURSOR
                Screen.gotoxy(12, 10 + (i * 2))

                value = input().strip()

                # VALIDAR VACIO
                if not self.validar_vacio(value):

                    Screen.gotoxy(1, 15)

                    Screen.error("El numero no puede estar vacío.")

                    continue


                # VALIDAR NUMERO
                try:

                    value = float(value)

                except ValueError:

                    Screen.gotoxy(1, 15)

                    Screen.error("Debe ingresar un numero valido.")

                    continue

                numbers.append(value)
                break

        # ==================================================
        # ORDENAR LISTA
        # ==================================================

        numbers.sort()

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Lista ordenada : {numbers}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()

    # ==================================================
    # PREGUNTA 2
    # ==================================================

    def b8question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Calcular suma, maximo y minimo de una lista.
    """)

        # ==================================================
        # LISTA
        # ==================================================

        numbers = [5, 3, 8, 1, 9, 3]

        # ==================================================
        # PROCESOS
        # ==================================================

        total = sum(numbers)

        maximum = max(numbers)

        minimum = min(numbers)

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Lista   : {numbers}

    Suma    : {total}

    Maximo  : {maximum}

    Minimo  : {minimum}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()

# ==================================================
# PREGUNTA 3
# ==================================================

    def b8question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. ¿Que pasa si haces: copia = lista y luego copia.append(4)?
    """)

        # ==================================================
        # LISTAS
        # ==================================================

        lista = [1, 2, 3]

        copia = lista

        # ==================================================
        # APPEND
        # ==================================================

        copia.append(4)

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Lista original : {lista}

    Copia          : {copia}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        print("""
    EXPLICACION:

    La lista original tambien cambia porque 'lista' y 'copia' apuntan al mismo
    objeto en memoria.
    """)

        Screen.pausa()

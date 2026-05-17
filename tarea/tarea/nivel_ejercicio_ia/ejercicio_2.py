from core import Screen
from core import PromedioMixin , ValidationMixin
# ==================================================
# CLASE CURSO
# ==================================================

class Curso(PromedioMixin):

    def __init__(self, nombre, notas):

        self.nombre = nombre
        self.notas = notas

    def mostrar(self):

        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
               CURSO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Curso      : {self.nombre}
Notas      : {self.notas}

Promedio   : {self.calcular_promedio(self.notas)}
Máxima     : {self.calcular_max(self.notas)}
Mínima     : {self.calcular_min(self.notas)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# FORMULARIO
# ==================================================

class Formulario2(ValidationMixin):

    def ejecutar(self):

        Screen.limpiar()

        Screen.titulo("EJERCICIO 2 - ESTADISTICAS")

        Screen.gotoxy(3, 4)
        print("=== INGRESAR DATOS ===")

        # ==================================================
        # ETIQUETAS
        # ==================================================

        Screen.gotoxy(1, 6)
        print("Curso:")

        Screen.gotoxy(1, 8)
        print("Nota 1:")

        Screen.gotoxy(1, 10)
        print("Nota 2:")

        Screen.gotoxy(1, 12)
        print("Nota 3:")

        Screen.gotoxy(1, 14)
        print("Nota 4:")

        Screen.gotoxy(1, 16)
        print("Nota 5:")

        # ==================================================
        # NOMBRE CURSO
        # ==================================================

        while True:

            # LIMPIAR ERROR
            Screen.gotoxy(1, 20)
            print(" " * 70, end="")

            # LIMPIAR INPUT
            Screen.gotoxy(12, 6)
            print(" " * 30, end="")

            # POSICION
            Screen.gotoxy(12, 6)

            nombre = input().strip()

            # VALIDAR VACIO
            if not self.validar_vacio(nombre):

                Screen.gotoxy(1, 19)

                Screen.error("El nombre no puede estar vacío.")

                continue

            # VALIDAR LETRAS
            if not self.validar_solo_letras(nombre):

                Screen.gotoxy(1, 19)

                Screen.error("El nombre solo debe tener letras.")

                continue

            nombre = self.normalizar_texto(nombre)

            break

        # ==================================================
        # NOTAS
        # ==================================================

        notas = []

        posiciones_y = [8, 10, 12, 14, 16]

        for i, y in enumerate(posiciones_y):

            while True:

                # LIMPIAR ERROR
                Screen.gotoxy(1, 20)
                print(" " * 70, end="")

                # LIMPIAR INPUT
                Screen.gotoxy(12, y)
                print(" " * 30, end="")

                # POSICION
                Screen.gotoxy(12, y)

                nota = input().strip()

                # VALIDAR VACIO
                if not self.validar_vacio(nota):

                    Screen.gotoxy(1, 19)

                    Screen.error(f"La nota {i+1} no puede estar vacía.")

                    continue

                # VALIDAR NOTA
                if not self.validar_nota(nota):

                    Screen.gotoxy(1, 19)

                    Screen.error(f"La nota {i+1} debe estar entre 0 y 10.")

                    continue

                notas.append(float(nota))

                break

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        curso = Curso(nombre, notas)

        print("\nRESPUESTA:\n")

        Screen.mostrar(curso.mostrar())

        Screen.pausa()
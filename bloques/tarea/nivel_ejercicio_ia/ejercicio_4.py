from core import Screen, ask_continuar
from core import ValidationMixin, IMCMixin


class Persona(IMCMixin):
    def __init__(self, nombre, peso, altura):

        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def mostrar(self):

        imc = self.calcular_imc(self.peso, self.altura)

        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            PERSONA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nombre : {self.nombre}

Peso   : {self.peso} kg

Altura : {self.altura} m

IMC    : {imc}

Estado : {self.clasificar(imc)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# FORMULARIO
# ==================================================


class Formulario4(ValidationMixin):
    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def ejecutar(self):

        Screen.limpiar()

        Screen.titulo("EJERCICIO 4 - IMC")

        Screen.gotoxy(3, 4)
        print("=== INGRESAR DATOS ===")

        # ==================================================
        # ETIQUETAS
        # ==================================================

        Screen.gotoxy(1, 6)
        print("Nombre:")

        Screen.gotoxy(1, 8)
        print("Peso (kg):")

        Screen.gotoxy(1, 10)
        print("Altura (m):")

        # ==================================================
        # NOMBRE
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(12, 6)
            print(" " * 30, end="")

            # POSICION
            Screen.gotoxy(12, 6)

            nombre = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 70, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(nombre):
                Screen.gotoxy(1, 14)

                Screen.error("El nombre no puede estar vacío.                       ")

                continue

            # VALIDAR LETRAS
            if not self.validar_solo_letras(nombre):
                Screen.gotoxy(1, 14)

                Screen.error("El nombre solo debe contener letras.                      ")

                continue

            nombre = self.normalizar_texto(nombre)

            break

        # ==================================================
        # PESO
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(13, 8)
            print(" " * 30, end="")

            # POSICION
            Screen.gotoxy(13, 8)

            peso = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 70, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(peso):
                Screen.gotoxy(1, 14)

                Screen.error("El peso no puede estar vacío.                         ")

                continue

            # VALIDAR NUMERO
            if not self.validar_numero_positivo(peso):
                Screen.gotoxy(1, 14)

                Screen.error("Ingrese un peso válido mayor a 0.                                 ")

                continue

            peso = float(peso)

            break

        # ==================================================
        # ALTURA
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(14, 10)
            print(" " * 30, end="")

            # POSICION
            Screen.gotoxy(14, 10)

            altura = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 14)
            print(" " * 70, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(altura):
                Screen.gotoxy(1, 14)

                Screen.error("La altura no puede estar vacía.                       ")

                continue

            # VALIDAR ALTURA
            if not self.validar_altura(altura):
                Screen.gotoxy(1, 14)

                Screen.error("Ingrese una altura válida (ej: 1.75).                     ")

                continue

            altura = float(altura)

            break

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        persona = Persona(nombre, peso, altura)

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(persona.mostrar())


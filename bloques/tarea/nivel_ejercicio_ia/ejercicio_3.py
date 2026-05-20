from core import Screen, ask_continuar
from core import ValidationMixin, TemperaturaMixin




# ==================================================
# CLASE SENSOR
# ==================================================

class Sensor(TemperaturaMixin):

    def __init__(self, nombre, celsius):

        self.nombre = nombre
        self.celsius = celsius

    def mostrar(self):

        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
               SENSOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sensor       : {self.nombre}

Celsius      : {self.celsius} °C

Fahrenheit   : {self.a_fahrenheit(self.celsius)} °F

Kelvin       : {self.a_kelvin(self.celsius)} K

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# FORMULARIO
# ==================================================

class Formulario3(ValidationMixin ,TemperaturaMixin):

    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def ejecutar(self):

        Screen.limpiar()

        Screen.titulo("EJERCICIO 3 - TEMPERATURA")

        Screen.gotoxy(3, 4)
        print("=== INGRESAR DATOS ===")

        # ==================================================
        # ETIQUETAS
        # ==================================================

        Screen.gotoxy(1, 6)
        print("Nombre Sensor:")

        Screen.gotoxy(1, 8)
        print("Temperatura °C:")

        # ==================================================
        # NOMBRE
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(18, 6)
            print(" " * 30, end="")

            # POSICION
            Screen.gotoxy(18, 6)

            nombre = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 12)
            print(" " * 70, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(nombre):

                Screen.gotoxy(1, 12)

                Screen.error("El nombre no puede estar vacío.                           ")

                continue

            # VALIDAR LETRAS
            if not self.validar_solo_letras(nombre):

                Screen.gotoxy(1, 12)

                Screen.error("El nombre solo debe contener letras.                                      ")

                continue

            nombre = self.normalizar_texto(nombre)

            break

        # ==================================================
        # TEMPERATURA
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(19, 8)
            print(" " * 30, end="")

            # POSICION
            Screen.gotoxy(19, 8)

            celsius = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 12)
            print(" " * 70, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(celsius):

                Screen.gotoxy(1, 12)

                Screen.error("La temperatura no puede estar vacía.                          ")

                continue

            # VALIDAR NUMERO
            if not self.validar_temperatura(celsius):

                Screen.gotoxy(1, 12)

                Screen.error("Ingrese una temperatura válida.                                   ")

                continue

            celsius = float(celsius)

            break

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        sensor = Sensor(nombre, celsius)

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(sensor.mostrar())

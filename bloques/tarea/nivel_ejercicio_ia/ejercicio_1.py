from core import Screen, ask_continuar
from core import DescuentoMixin, ValidationMixin


class Producto(DescuentoMixin, ValidationMixin):
    def __init__(self, nombre, precio, porcentaje):

        self.nombre = nombre
        self.precio = precio
        self.porcentaje = porcentaje

    def mostrar(self):

        final = self.calcular_descuento(self.precio, self.porcentaje)

        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
              PRODUCTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nombre      : {self.nombre}
Precio      : ${self.precio}
Descuento   : {self.porcentaje}%
Total Final : ${final}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# FORMULARIO
# ==================================================


class Formulario1(ValidationMixin):
    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def ejecutar(self):

        Screen.limpiar()

        Screen.titulo("EJERCICIO 1 - DESCUENTO")

        Screen.gotoxy(3, 4)
        print("=== INGRESAR DATOS ===")

        # ==================================================
        # ETIQUETAS
        # ==================================================

        Screen.gotoxy(1, 6)
        print("Nombre:")

        Screen.gotoxy(1, 8)
        print("Precio:")

        Screen.gotoxy(1, 10)
        print("Descuento %:")

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
            Screen.gotoxy(1, 13)
            print(" " * 70, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(nombre):
                Screen.gotoxy(1, 13)

                Screen.error("El nombre no puede estar vacío.                            ")

                continue

            # VALIDAR LETRAS
            if not self.validar_solo_letras(nombre):
                Screen.gotoxy(1, 13)

                Screen.error("El nombre solo debe tener letras.                         ")

                continue

            nombre = self.normalizar_texto(nombre)

            break

        # ==================================================
        # PRECIO
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(12, 8)
            print(" " * 30, end="")

            # POSICION
            Screen.gotoxy(12, 8)

            precio = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 13)
            print(" " * 70, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(precio):
                Screen.gotoxy(1, 13)

                Screen.error("El precio no puede estar vacío.                               ")

                continue

            # VALIDAR PRECIO
            if not self.validar_numero_positivo(precio):
                Screen.gotoxy(1, 13)

                Screen.error("Ingrese un precio válido.                                         ")

                continue

            precio = float(precio)

            break

        # ==================================================
        # DESCUENTO
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(15, 10)
            print(" " * 30, end="")

            # POSICION
            Screen.gotoxy(15, 10)

            porcentaje = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 13)
            print(" " * 70, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(porcentaje):
                Screen.gotoxy(1, 13)

                Screen.error("El descuento no puede estar vacío.                            ")

                continue

            # VALIDAR PORCENTAJE
            if not self.validar_porcentaje(porcentaje):
                Screen.gotoxy(1, 13)

                Screen.error("Ingrese un porcentaje válido.                                 ")

                continue

            porcentaje = float(porcentaje)

            break

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        producto = Producto(nombre, precio, porcentaje)

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(producto.mostrar())


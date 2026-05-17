from core import Screen, JsonManager, ValidationMixin

# ==================================================
# EMPLEADO
# ==================================================


class Empleado:
    ARCHIVO = "data/empleados.json"

    def __init__(self, nombre, cargo, salario, departamento):

        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.departamento = departamento

    # ==================================================
    # GUARDAR
    # ==================================================

    def guardar(self):

        datos = JsonManager.load(self.ARCHIVO)

        datos.append(
            {
                "nombre": self.nombre,
                "cargo": self.cargo,
                "salario": self.salario,
                "departamento": self.departamento,
            }
        )

        JsonManager.save(self.ARCHIVO, datos)

    # ==================================================
    # MOSTRAR
    # ==================================================

    def mostrar(self):

        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            EMPLEADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nombre        : {self.nombre}
Cargo         : {self.cargo}
Salario       : ${self.salario}
Departamento  : {self.departamento}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    # ==================================================
    # MOSTRAR TODOS
    # ==================================================

    @staticmethod
    def mostrar_todos():

        datos = JsonManager.load(Empleado.ARCHIVO)

        if not datos:
            Screen.error("No hay empleados registrados.")

            return

        bloques = []

        for d in datos:
            empleado = Empleado(
                d["nombre"], d["cargo"], d["salario"], d["departamento"]
            )

            bloques.append(empleado.mostrar())

        Screen.mostrar_grid(bloques, columnas=2, ancho_total=90)


# ==================================================
# FORMULARIO
# ==================================================


class Formulario5(ValidationMixin):
    def ejecutar(self):

        while True:
            # ==================================================
            # MENU
            # ==================================================

            Screen.limpiar()

            Screen.titulo("EJERCICIO 7 - EMPLEADOS JSON")

            print("""
    1. Registrar empleado
    2. Ver empleados
    3. Salir
            """)

            Screen.gotoxy(1, 12)

            print("Opcion:")

            Screen.gotoxy(10, 12)

            opcion = input().strip()

            # ==================================================
            # REGISTRAR
            # ==================================================

            if opcion == "1":
                Screen.limpiar()

                Screen.titulo("REGISTRAR EMPLEADO")

                # ==================================================
                # ETIQUETAS
                # ==================================================

                Screen.gotoxy(1, 8)
                print("Nombre:")

                Screen.gotoxy(1, 10)
                print("Cargo:")

                Screen.gotoxy(1, 12)
                print("Salario:")

                Screen.gotoxy(1, 14)
                print("Departamento:")

                # ==================================================
                # NOMBRE
                # ==================================================

                while True:
                    Screen.gotoxy(1, 17)
                    print(" " * 70, end="")

                    Screen.gotoxy(12, 8)
                    print(" " * 30, end="")

                    Screen.gotoxy(12, 8)

                    nombre = input().strip()

                    # VALIDAR VACIO
                    if not self.validar_vacio(nombre):
                        Screen.gotoxy(1, 16)

                        Screen.error("El nombre no puede estar vacío.")

                        continue

                    # VALIDAR LETRAS
                    if not self.validar_solo_letras(nombre):
                        Screen.gotoxy(1, 16)

                        Screen.error("El nombre solo debe tener letras.")

                        continue

                    nombre = self.normalizar_texto(nombre)

                    break

                # ==================================================
                # CARGO
                # ==================================================

                while True:
                    Screen.gotoxy(1, 17)
                    print(" " * 70, end="")

                    Screen.gotoxy(12, 10)
                    print(" " * 30, end="")

                    Screen.gotoxy(12, 10)

                    cargo = input().strip()

                    # VALIDAR VACIO
                    if not self.validar_vacio(cargo):
                        Screen.gotoxy(1, 16)

                        Screen.error("El cargo no puede estar vacío.")

                        continue

                    # VALIDAR LETRAS
                    if not self.validar_solo_letras(cargo):
                        Screen.gotoxy(1, 16)

                        Screen.error("El cargo solo debe tener letras.")

                        continue

                    cargo = self.normalizar_texto(cargo)

                    break

                # ==================================================
                # SALARIO
                # ==================================================

                while True:
                    Screen.gotoxy(1, 17)
                    print(" " * 70, end="")

                    Screen.gotoxy(12, 12)
                    print(" " * 30, end="")

                    Screen.gotoxy(12, 12)

                    salario = input().strip()

                    # VALIDAR VACIO
                    if not self.validar_vacio(salario):
                        Screen.gotoxy(1, 16)

                        Screen.error("El salario no puede estar vacío.")

                        continue

                    # VALIDAR PRECIO
                    if not self.validar_numero_positivo(salario):
                        Screen.gotoxy(1, 16)

                        Screen.error("Ingrese un salario válido.")

                        continue

                    salario = float(salario)

                    break

                # ==================================================
                # DEPARTAMENTO
                # ==================================================

                while True:
                    Screen.gotoxy(1, 17)
                    print(" " * 70, end="")

                    Screen.gotoxy(18, 14)
                    print(" " * 30, end="")

                    Screen.gotoxy(18, 14)

                    departamento = input().strip()

                    # VALIDAR VACIO
                    if not self.validar_vacio(departamento):
                        Screen.gotoxy(1, 16)

                        Screen.error("El departamento no puede estar vacío.")

                        continue

                    # VALIDAR LETRAS
                    if not self.validar_solo_letras(departamento):
                        Screen.gotoxy(1, 16)

                        Screen.error("El departamento solo debe tener letras.")

                        continue

                    departamento = self.normalizar_texto(departamento)

                    break

                # ==================================================
                # GUARDAR
                # ==================================================

                empleado = Empleado(nombre, cargo, salario, departamento)

                empleado.guardar()

                Screen.limpiar()

                Screen.exito("Empleado guardado correctamente.")

                print()

                Screen.mostrar(empleado.mostrar())

                Screen.pausa()

            # ==================================================
            # VER EMPLEADOS
            # ==================================================

            elif opcion == "2":
                Screen.limpiar()

                Screen.titulo("TODOS LOS EMPLEADOS")

                print("\nRESPUESTA:\n")

                Empleado.mostrar_todos()

                Screen.pausa()

            # ==================================================
            # SALIR
            # ==================================================

            elif opcion == "3":
                Screen.limpiar()

                Screen.aviso("Hasta luego.")

                break

            # ==================================================
            # ERROR
            # ==================================================

            else:
                Screen.error("Opcion invalida.")

                Screen.pausa()

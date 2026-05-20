from core import Screen, PromedioMixin, ValidationMixin, ValidacionUsuarioMixin, ExportarMixin, ask_continuar


# ==================================================
# CLASE p1
# ==================================================

class Estudiante(PromedioMixin):

    def __init__(self, nombre, notas):

        self.nombre = nombre

        self.notas = notas

    def mostrar_promedio(self):

        promedio = self.calcular_promedio(self.notas)

        Screen.mostrar(f"""

            ESTUDIANTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nombre      : {self.nombre}

Notas       : {self.notas}

Promedio    : {promedio}


""")

# ==================================================
# CLASE p2
# ==================================================

class Usuario(ValidacionUsuarioMixin):

    def __init__(self, nombre, correo, edad):

        self.nombre = nombre

        self.correo = correo

        self.edad = edad

    def registrar(self):

        Screen.mostrar(f"""

            USUARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nombre   : {self.nombre}

Correo   : {self.correo}

Edad     : {self.edad}

Estado   : REGISTRADO


""")


# ==================================================
# CLASE p3
# ==================================================

class Reporte(ExportarMixin):

    def __init__(self, datos):
        self.datos = datos

    def mostrar_reporte(self):

        json_data = self.exportar_json(self.datos)
        csv_data = self.exportar_csv(self.datos)

        Screen.mostrar(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            REPORTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DATOS:

{self.datos}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

        bloque_json = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        FORMATO JSON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{json_data}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

        bloque_csv = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        FORMATO CSV
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{csv_data}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

        Screen.mostrar_grid([bloque_json, bloque_csv], columnas=2, ancho_total=100)


class Bloque_17(ValidationMixin):

    # ==================================================
    # PREGUNTA 1
    # ==================================================

    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def b17question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Crea PromedioMixin con calcular_promedio(notas) e intégralo.
o El mixin debe contener un método que reciba una lista de notas numéricas.
o El método debe calcular y devolver el promedio.
o Luego, crea una clase como Estudiante que herede del mixin y use ese método para
  mostrar el promedio final del alumno.
o Ejemplo esperado: si las notas son [8, 9, 10], el promedio debe ser 9.0.
""")

        # ==================================================
        # ETIQUETAS
        # ==================================================

        Screen.gotoxy(5, 11)
        print("===== INGRESAR DATOS =====")

        Screen.gotoxy(1, 13)
        print("Nombre:")

        Screen.gotoxy(1, 15)
        print("Nota 1:")

        Screen.gotoxy(1, 17)
        print("Nota 2:")

        Screen.gotoxy(1, 19)
        print("Nota 3:")

        # ==================================================
        # NOMBRE
        # ==================================================

        while True:

            # LIMPIAR INPUT
            Screen.gotoxy(12, 13)
            print(" " * 30, end="")

            # POSICION CURSOR
            Screen.gotoxy(12, 13)

            nombre = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 21)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(nombre):

                Screen.gotoxy(1, 21)

                Screen.error("El nombre no puede estar vacío.                       ")

                continue

            # VALIDAR LETRAS
            if not self.validar_solo_letras(nombre):

                Screen.gotoxy(1, 21)

                Screen.error("Solo se permiten letras.                                  ")

                continue

            # NORMALIZAR
            nombre = self.normalizar_texto(nombre)

            break

        # ==================================================
        # NOTAS
        # ==================================================

        notas = []

        for i, y in enumerate([15, 17, 19]):

            while True:

                # LIMPIAR INPUT
                Screen.gotoxy(12, y)
                print(" " * 30, end="")

                # POSICION CURSOR
                Screen.gotoxy(12, y)

                nota = input().strip()

                # LIMPIAR ERROR
                Screen.gotoxy(1, 21)
                print(" " * 100, end="")

                # VALIDAR VACIO
                if not self.validar_vacio(nota):

                    Screen.gotoxy(1, 21)

                    Screen.error(f"La nota {i + 1} no puede estar vacía.                            ")

                    continue

                # VALIDAR NUMERO
                try:

                    nota = float(nota)

                except ValueError:

                    Screen.gotoxy(1, 21)

                    Screen.error(f"La nota {i + 1} debe ser numérica.                                   ")

                    continue

                # VALIDAR RANGO
                if nota < 0 or nota > 10:

                    Screen.gotoxy(1, 21)

                    Screen.error(f"La nota {i + 1} debe estar entre 0 y 10.                                 ")

                    continue

                notas.append(nota)

                break

        # ==================================================
        # OBJETO
        # ==================================================

        student = Estudiante(nombre, notas)

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        Screen.aviso("\nRESPUESTA:\n")

        student.mostrar_promedio()


    # ==================================================
    # PREGUNTA 2
    # ==================================================

    @ask_continuar("¿Desea continuar? (1=Sí / 2=Menú): ")
    def b17question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Crear ValidacionMixin con:
- validar_email(correo)
- validar_edad(edad) e integrarlo en una clase Usuario.
""")

        # ==================================================
        # ETIQUETAS
        # ==================================================

        Screen.gotoxy(5, 10)
        print("===== INGRESAR DATOS =====")

        Screen.gotoxy(1, 12)
        print("Nombre:")

        Screen.gotoxy(1, 14)
        print("Correo:")

        Screen.gotoxy(1, 16)
        print("Edad:")

        # ==================================================
        # NOMBRE
        # ==================================================

        while True:
            # LIMPIAR INPUT
            Screen.gotoxy(9, 12)
            print(" " * 30, end="")

            # CURSOR
            Screen.gotoxy(9, 12)

            nombre = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 19)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(nombre):
                Screen.gotoxy(1, 19)

                Screen.error("El nombre no puede estar vacío.                                           ")

                continue

            # VALIDAR LETRAS
            if not self.validar_solo_letras(nombre):
                Screen.gotoxy(1, 19)

                Screen.error("Solo se permiten letras.                                                      ")

                continue

            nombre = self.normalizar_texto(nombre)

            break

        # ==================================================
        # CORREO
        # ==================================================

        while True:
            # LIMPIAR INPUT
            Screen.gotoxy(9, 14)
            print(" " * 40, end="")

            # CURSOR
            Screen.gotoxy(9, 14)

            correo = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 19)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(correo):
                Screen.gotoxy(1, 19)

                Screen.error("El correo no puede estar vacío.                                                               ")

                continue

            # VALIDAR EMAIL
            if not Usuario.validar_email(correo):
                Screen.gotoxy(1, 19)

                Screen.error("Correo inválido.                                                                              ")

                continue

            break

        # ==================================================
        # EDAD
        # ==================================================

        while True:
            # LIMPIAR INPUT
            Screen.gotoxy(9, 16)
            print(" " * 30, end="")

            # CURSOR
            Screen.gotoxy(9, 16)

            edad = input().strip()

            # LIMPIAR ERROR
            Screen.gotoxy(1, 19)
            print(" " * 100, end="")

            # VALIDAR VACIO
            if not self.validar_vacio(edad):
                Screen.gotoxy(1, 19)

                Screen.error("La edad no puede estar vacía.                                                     ")

                continue

            # VALIDAR NUMERO
            try:
                edad = int(edad)

            except ValueError:
                Screen.gotoxy(1, 19)

                Screen.error("Debe ingresar una edad válida.                                                        ")

                continue

            # VALIDAR EDAD
            if not Usuario.validar_edad(edad):
                Screen.gotoxy(1, 19)

                Screen.error("Debe ser mayor de edad.                                                                   ")

                continue

            break

        # ==================================================
        # OBJETO
        # ==================================================

        user = Usuario(nombre, correo, edad)

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        Screen.aviso("\nRESPUESTA:\n")

        user.registrar()


    # ==================================================
    # PREGUNTA 3
    # ==================================================

    def b17question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Crear ExportarMixin con:
- exportar_json(datos)
- exportar_csv(datos) e integrarlo en una clase Reporte.
""")

        # ==================================================
        # DATOS
        # ==================================================

        products = [

            {
                "nombre": "Laptop",
                "precio": 1200
            },

            {
                "nombre": "Mouse",
                "precio": 25
            }

        ]

        # ==================================================
        # OBJETO
        # ==================================================

        report = Reporte(products)

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")

        report.mostrar_reporte()


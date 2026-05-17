from core import Screen, ValidationMixin
# ==================================================
# CLASE PRODUCTO
# ==================================================
class Product:
    def __init__(self, code, name, price):
        if price < 0:
            raise ValueError("El precio no puede ser negativo")
        self.code = code
        self.name = name
        self.price = price

    def show_product(self):
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        INFORMACION PRODUCTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Codigo : {self.code}
Nombre : {self.name}
Precio : ${self.price}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# CLASE ESTUDIANTE
# ==================================================
class Student:
    def __init__(self, name, grades=None):
        self.name = name
        if grades is None:
            self.grades = []
        else:
            self.grades = grades

    def show_student(self):
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        INFORMACION ESTUDIANTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Nombre : {self.name}
Notas  : {self.grades}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    # ==============================================
    # CLASSMETHOD
    # ==============================================
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["grades"])


class Bloque_1(ValidationMixin):
    # ==================================================
    # PREGUNTA 1
    # ==================================================
    def b1question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Crea la clase Producto con codigo, nombre y precio. Instancia 2 productos.
2. Agrega validacion para que el precio no sea negativo.
    """)

        print("\nINGRESE LOS DATOS DEL PRODUCTO 1:\n")

        Screen.gotoxy(1, 11)
        print("Codigo:")

        Screen.gotoxy(1, 13)
        print("Nombre:")

        Screen.gotoxy(1, 15)
        print("Precio:")

        # ==================================================
        # CODIGO
        # ==================================================
        while True:
            Screen.gotoxy(10, 11)
            print(" " * 30, end="")

            Screen.gotoxy(10, 11)
            code = input().strip()

            Screen.gotoxy(1, 18)
            print(" " * 60, end="")

            if not self.validar_vacio(code):
                Screen.gotoxy(1, 18)
                Screen.error("El Codigo no puede estar vacío.")
                continue
            break

        # ==================================================
        # NOMBRE
        # ==================================================
        while True:
            Screen.gotoxy(10, 13)
            print(" " * 30, end="")

            Screen.gotoxy(10, 13)
            name = input().strip()

            Screen.gotoxy(1, 18)
            print(" " * 60, end="")

            if not self.validar_vacio(name):
                Screen.gotoxy(1, 18)
                Screen.error("El nombre no puede estar vacío.")
                continue

            if not self.validar_solo_letras(name):
                Screen.gotoxy(1, 18)
                Screen.error("El nombre solo debe contener letras.")
                continue

            name = self.normalizar_texto(name)
            break

        # ==================================================
        # PRECIO
        # ==================================================
        while True:
            Screen.gotoxy(10, 15)
            print(" " * 30, end="")

            Screen.gotoxy(10, 15)
            price = input().strip()

            Screen.gotoxy(1, 18)
            print(" " * 60, end="")

            if not self.validar_vacio(price):
                Screen.gotoxy(1, 18)
                Screen.error("El Precio no puede estar vacío.")
                continue

            try:
                price = float(price)
            except ValueError:
                Screen.gotoxy(1, 18)
                Screen.error("El Precio debe ser numerico.")
                continue

            if not self.validar_numero_positivo(price):
                Screen.gotoxy(1, 18)
                Screen.error("El Precio debe ser mayor a 0.")
                continue
            break

        Screen.limpiar()

        product3 = Product(code, name, price)
        product1 = Product("P001", "Laptop", 900)
        product2 = Product("P002", "Mouse", 25)

        print("\nRESPUESTA:\n")

        Screen.mostrar_grid([
            product1.show_product(),
            product2.show_product(),
            product3.show_product(),
        ], columnas=3, ancho_total=120)

        Screen.pausa()

    # ==================================================
    # PREGUNTA 2
    # ==================================================

    def b1question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
3. Crea Estudiante con nombre y notas = None.
4. Agrega un @classmethod desde_diccionario.
""")

        print("\nINGRESE LOS DATOS DEL ESTUDIANTE:\n")

        Screen.gotoxy(1, 11)
        print("Nombre:")

        Screen.gotoxy(1, 13)
        print("Nota 1:")

        Screen.gotoxy(1, 15)
        print("Nota 2:")

        Screen.gotoxy(1, 17)
        print("Nota 3:")

        Screen.gotoxy(1, 19)
        print("Nota 4:")

        # ==================================================
        # NOMBRE
        # ==================================================
        while True:
            Screen.gotoxy(1, 22)
            print(" " * 100, end="")

            Screen.gotoxy(10, 11)
            print(" " * 30, end="")

            Screen.gotoxy(10, 11)
            name = input().strip()

            Screen.gotoxy(1, 21)
            print(" " * 60, end="")

            if not self.validar_vacio(name):
                Screen.gotoxy(1, 21)
                print(Screen.ROJO + "El nombre no puede estar vacío." + Screen.RESET)
                continue

            if not self.validar_solo_letras(name):
                Screen.gotoxy(1, 21)
                print(Screen.ROJO + "El nombre solo debe contener letras." + Screen.RESET)
                continue

            name = self.normalizar_texto(name)
            break

        # ==================================================
        # NOTAS
        # ==================================================
        student3 = Student(name)
        for i in range(4):
            y = 13 + (i * 2)
            while True:
                Screen.gotoxy(1, 22)
                print(" " * 100, end="")

                Screen.gotoxy(10, y)
                print(" " * 30, end="")

                Screen.gotoxy(10, y)
                grade = input().strip()

                if not self.validar_vacio(grade):
                    Screen.gotoxy(1, 21)
                    Screen.error(f"La nota {i + 1} no puede estar vacía.    ")
                    continue

                try:
                    grade = float(grade)
                except ValueError:
                    Screen.gotoxy(1, 21)
                    Screen.error(f"La nota {i + 1} debe ser numerica.     ")
                    continue

                if grade < 0 or grade > 10:
                    Screen.gotoxy(1, 21)
                    Screen.error(f"La nota {i + 1} debe estar entre 0 y 10.")
                    continue

                student3.grades.append(grade)
                break

        Screen.limpiar()

        # ==================================================
        # OBJETOS
        # ==================================================
        student1 = Student("Angel")
        student2 = Student("Carlos", [10, 9, 8])
        data = {"name": "Maria", "grades": [9, 10, 8]}
        student = Student.from_dict(data)

        # ==================================================
        # RESPUESTA
        # ==================================================
        print("\nRESPUESTA:\n")

        Screen.mostrar_grid([
            student1.show_student(),
            student2.show_student(),
            student.show_student(),
            student3.show_student(),
        ], columnas=2, ancho_total=90)

        Screen.pausa()
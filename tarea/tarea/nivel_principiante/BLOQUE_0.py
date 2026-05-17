from core import Screen


# ==================================================
# CLASE USER
# ==================================================


class User:
    def __init__(self, user_id, name, age, phone):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.phone = phone

    def show_user(self):
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         INFORMACION DEL USUARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID Usuario : {self.user_id}
Nombre     : {self.name}
Edad       : {self.age}
Celular    : {self.phone}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# CLASE AUTHOR
# ==================================================


class Author:
    def __init__(self, author_id, name, nationality):
        self.author_id = author_id
        self.name = name
        self.nationality = nationality

    def show_author(self):
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
          INFORMACION DEL AUTOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID Autor      : {self.author_id}
Nombre        : {self.name}
Nacionalidad  : {self.nationality}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# CLASE CATEGORY
# ==================================================


class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name

    def show_category(self):
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       INFORMACION DE LA CATEGORIA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID Categoria : {self.category_id}
Nombre       : {self.name}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# CLASE BOOK
# ==================================================


class Book:
    def __init__(self, book_id, title, author, category, pages, available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.pages = pages
        self.available = available

    def show_book(self):
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
         INFORMACION DEL LIBRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID Libro    : {self.book_id}
Titulo      : {self.title}
Autor       : {self.author.name}
Categoria   : {self.category.name}
Paginas     : {self.pages}
Disponible  : {"Si" if self.available else "No"}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# CLASE LOAN
# ==================================================


class Loan:
    def __init__(self, loan_id, user, book, loan_date, status):
        self.loan_id = loan_id
        self.user = user
        self.book = book
        self.loan_date = loan_date
        self.status = status

    def show_loan(self):
        return f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       INFORMACION DEL PRESTAMO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID Prestamo : {self.loan_id}
Usuario     : {self.user.name}
Libro       : {self.book.title}
Fecha       : {self.loan_date}
Estado      : {self.status}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# CLASE PERSON
# ==================================================


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person(self):
        return f"""
━━━━━━━━━━━━━━━━━━━━━━
   INFORMACION PERSONA
━━━━━━━━━━━━━━━━━━━━━━

Nombre : {self.name}
Edad   : {self.age}

━━━━━━━━━━━━━━━━━━━━━━
"""


# ==================================================
# CLASE BLOQUE 0
# ==================================================


class Bloque_0():

    # ==================================================
    # PREGUNTA 1
    # ==================================================

    def question_1(self):

        Screen.limpiar()
        Screen.titulo("PREGUNTA 1")

        print("""
Identifica 5 clases para modelar un sistema de biblioteca.
""")

        print("""
RESPUESTA:

1. User
2. Author
3. Category
4. Book
5. Loan
""")

        Screen.pausa()

    # ==================================================
    # PREGUNTA 2
    # ==================================================

    def question_2(self):

        Screen.limpiar()
        Screen.titulo("PREGUNTA 2")

        print("""
Crea la clase Persona con nombre y edad.
Instancia 3 objetos diferentes.
""")

        person1 = Person("Angel", 18)
        person2 = Person("Carlos", 20)
        person3 = Person("Maria", 19)

        Screen.respuesta()

        Screen.mostrar_grid([
            person1.show_person(),
            person2.show_person(),
            person3.show_person(),
        ], columnas=3, ancho_total=80)

        Screen.pausa()

    # ==================================================
    # PREGUNTA 3
    # ==================================================

    def question_3(self):

        Screen.limpiar()
        Screen.titulo("PREGUNTA 3")

        print("""
Explica con tus palabras la diferencia entre clase y objeto.
""")

        print("""
RESPUESTA:

Una clase es un molde o plantilla
que define atributos y métodos.

Un objeto es una instancia creada
a partir de una clase.

Ejemplo:

Clase  -> Person
Objeto -> person1
""")

        print("""
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                EJEMPLO COMPLETO
                    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

        user1     = User(1, "Angel", 18, "0943290197")
        author1   = Author(1, "Gabriel Garcia Marquez", "Colombiano")
        category1 = Category(1, "Programacion")
        book1     = Book(1, "Python Basics", author1, category1, 500, True)
        loan1     = Loan(1, user1, book1, "2026-05-09", "Pendiente")

        Screen.mostrar_grid([
            user1.show_user(),
            author1.show_author(),
            category1.show_category(),
            book1.show_book(),
            loan1.show_loan(),
        ], columnas=2, ancho_total=90)

        Screen.pausa()
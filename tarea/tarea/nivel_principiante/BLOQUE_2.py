from core import Screen

class Example:
    def show_data(self):
        text = "Python"
        name = ["Carlos", "Maria", "Angel"]

        info = {"city": "Milagro", "country": "Ecuador"}


        print(f"Texto: {text}")
        print(f"Primer caracter : {text[0]}")

        print(f"\nLista: {name}")
        print(f"Ultimo elemento : {name[-1]}")

        print(f"\nDiccionario {info}")
        print(f"Valor del dict  : {info['country']}")

class Bloque_2():
# ==================================================
# PREGUNTA 1
# ==================================================
    def b2question_1(self):
        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Declara una variable de cada tipo simple y complejo e imprimelas.
    """)
        # Variable simples
        name = "Angel"
        age = 18
        height = 1.75
        active = True

        # Variable complejas
        subjects = ["Python", "POO", "Base Datos"]

        data = {"city": "Milagro", "country": "Ecuador"}

        print("""
RESPUESTA:""")
        print("""
            Variable simples
            """)
        print(f"String  : {name}")
        print(f"Integer : {age}")
        print(f"Float   : {height}")
        print(f"Boolean : {active}")

        print(
            """
            Variable complejas
            """
        )
        print(f"Lista   : {subjects}")

        print(f"Diccionario : {data}")
        Screen.pausa()


    # ==================================================
    # PREGUNTA 2
    # ==================================================
    def b2question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Crea una lista con 5 elementos. Imprime el primero, el ultimo y lista[1:4].
    """)
        numbers = [10, 20, 30, 40, 50]

        print("""
RESPUESTA:
            """)
        print(f"Lista completa : {numbers}")

        print(f"\nPrimer elemento : {numbers[0]}")

        print(f"Ultimo elemento : {numbers[-1]}")

        print(f"lista[1:4] : {numbers[1:4]}")

        Screen.pausa()


    # ==================================================
    # PREGUNTA 3
    # ==================================================


    def b2question_3(self):
        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Crea una clase con un metodo que declare un str, una list y un dict.
    Imprimir: primer carácter del texto, último elemento de la lista, valor de una clave del dict. 
    """)

        print("""
    RESPUESTA
                """)
        example = Example()
        example.show_data()
        Screen.pausa()
        


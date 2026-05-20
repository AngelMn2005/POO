from core import Screen,JsonManager
import os

class Bloque_16():
    # ==================================================
    # PREGUNTA 1
    # ==================================================

    def b16question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Escribe "Python" en un archivo y luego leelo.
    """)

        # ==================================================
        # CREAR CARPETA DATA
        # ==================================================

        os.makedirs("data", exist_ok=True)

        # ==================================================
        # ESCRIBIR ARCHIVO
        # ==================================================

        with open("data/python.txt", "w") as file:

            file.write("Python\n")

        # ==================================================
        # LEER ARCHIVO
        # ==================================================

        with open("data/python.txt", "r") as file:

            content = file.read()

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(f"""

                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Contenido:

    {content}


    """)

        Screen.pausa()
    # ==================================================
    # PREGUNTA 2
    # ==================================================

    def b16question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Guarda {"x":10, "y":20} en JSON y vuelve a cargarlo.
    """)

        # ==================================================
        # DATOS
        # ==================================================

        data = {
            "x": 10,
            "y": 20
        }

        # ==================================================
        # GUARDAR JSON
        # ==================================================

        JsonManager.save("data/data.json", data)

        # ==================================================
        # CARGAR JSON
        # ==================================================

        result = JsonManager.load("data/data.json")

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")

        Screen.mostrar(f"""

                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Datos cargados:

    {result}


    """)

        Screen.pausa()

    # ==================================================
    # PREGUNTA 3
    # ==================================================

    def b16question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. Guarda una lista de usuarios en JSON y recorre con for.
    """)

        # ==================================================
        # LISTA
        # ==================================================

        users = [
            {"nombre": "Angel"},
            {"nombre": "Carlos"}
        ]

        # ==================================================
        # GUARDAR JSON
        # ==================================================

        JsonManager.save("data/users.json", users)

        # ==================================================
        # CARGAR JSON
        # ==================================================

        data = JsonManager.load("data/users.json")

        # ==================================================
        # RESPUESTA
        # ==================================================

        Screen.aviso("\nRESPUESTA:\n")

        print("""

                USUARIOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        for user in data:

            print(f"Nombre -> {user['nombre']}")

        print("""

    """)

        Screen.pausa()
from core import Screen

class Bloque_10():

    # ==================================================
    # PREGUNTA 1
    # ==================================================

    def b10question_1(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 1")

        print("""
1. Crear un diccionario de persona y acceder con [] y get().
    """)

        # ==================================================
        # DICCIONARIO
        # ==================================================

        person = {
            "name": "Angel",
            "age": 18,
            "city": "Milagro"
        }

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                DICCIONARIO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Persona : {person}

    Nombre  : {person['name']}

    Edad    : {person.get('age')}

    Ciudad  : {person['city']}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()


# ==================================================
# PREGUNTA 2
# ==================================================

    def b10question_2(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 2")

        print("""
2. Iterar sobre items() e imprimir clave y valor.
    """)

        # ==================================================
        # DICCIONARIO
        # ==================================================

        person = {
            "name": "Angel",
            "age": 18,
            "city": "Milagro"
        }

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                DICCIONARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Persona : {person}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        # ==================================================
        # RECORRER ITEMS
        # ==================================================

        for key, value in person.items():

            print(f"{key} -> {value}")

        print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        Screen.pausa()
                        


# ==================================================
# PREGUNTA 3
# ==================================================

    def b10question_3(self):

        Screen.limpiar()

        Screen.titulo("PREGUNTA 3")

        print("""
3. ¿Que pasa si haces: copia = datos y luego copia["b"] = 2?
    """)

        # ==================================================
        # DICCIONARIOS
        # ==================================================

        datos = {"a": 1}

        copia = datos

        # ==================================================
        # AGREGAR NUEVO VALOR
        # ==================================================

        copia["b"] = 2

        # ==================================================
        # RESPUESTA
        # ==================================================

        print("\nRESPUESTA:\n")

        print(f"""
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RESULTADO
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    datos : {datos}

    copia : {copia}

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)

        print("""
    EXPLICACION:

    Ambas variables apuntan al mismo diccionario en memoria.

    Por eso 'datos' tambien cambia.

    Para evitarlo se usa: datos.copy()
    """)

        Screen.pausa()
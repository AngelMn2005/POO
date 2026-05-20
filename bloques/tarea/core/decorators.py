from .screen import Screen

# ==================================================
# DECORADOR 1
# ==================================================

def iniciar(func):

    def wrapper():

        print("Iniciando...")

        func()

    return wrapper


# ==================================================
# DECORADOR 2
# ==================================================

def positivo(func):

    def wrapper(number):

        if number < 0:
            print("El numero debe ser positivo.")
            return None
        return func(number)

    return wrapper


# ==================================================
# DECORADOR 3
# ==================================================

def log(func):

    def wrapper(a, b):

        print("Llamando funcion...")

        return func(a, b)

    return wrapper

# ==================================================
# DECORADOR 4
# ==================================================

def ask_continuar(mensaje):
    # Función principal del decorador
    # Recibe el mensaje que se mostrará al usuario
    def decorador(func):
        # Esta función recibe la función original que será decorada
        def wrapper(*args, **kwargs):

            while True:
                # Ejecuta la función original (create, read, etc.)
                func(*args, **kwargs)

                while True:
                    # El mensaje va dentro del input() para evitar
                    # que el Enter de Screen.pausa() lo dispare
                    opcion = input(Screen.AMARILLO + mensaje + Screen.RESET).strip()

                    if not opcion:
                        # Valida vacío
                        Screen.aviso("No puede estar vacío. Solo 1 o 2.")
                        continue

                    if opcion == "1":
                        # Si elige 1 → repetir proceso
                        break

                    elif opcion == "2":
                        # Si elige 2 → salir al menú
                        Screen.aviso("Regresando al menú...")
                        return False

                    else:
                        # Si escribe algo inválido
                        Screen.aviso("Opción inválida. Solo se permite 1 o 2.")

        return wrapper
    return decorador

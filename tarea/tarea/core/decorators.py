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
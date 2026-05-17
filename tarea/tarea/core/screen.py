import os


class Screen():

    # Colores ANSI
    ROJO = "\033[31m"
    VERDE = "\033[32m"
    AMARILLO = "\033[33m"
    AZUL = "\033[34m"
    CYAN = "\033[36m"
    BLANCO = "\033[37m"
    RESET = "\033[0m"

    @staticmethod
    def limpiar():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def gotoxy(x, y):
        print(f"\033[{y};{x}H", end="")

    @staticmethod
    def titulo(texto: str):
        print(Screen.CYAN + "=" * 80 + Screen.RESET)
        print(Screen.AZUL + texto.center(80) + Screen.RESET)
        print(Screen.CYAN + "=" * 80 + Screen.RESET)

    @staticmethod
    def tituloExito(texto: str):
        print(Screen.VERDE + "=" * 80 + Screen.RESET)
        print(Screen.VERDE + texto.center(80) + Screen.RESET)
        print(Screen.VERDE + "=" * 80 + Screen.RESET)

    @staticmethod
    def exito(texto: str):
        print(Screen.VERDE + texto + Screen.RESET)

    @staticmethod
    def error(texto: str):
        print(Screen.ROJO + texto + Screen.RESET)

    @staticmethod
    def aviso(texto: str):
        print(Screen.AMARILLO + texto + Screen.RESET)

    @staticmethod
    def pausa():
        input(Screen.BLANCO + "\nPresione Enter para continuar..." + Screen.RESET)

    @staticmethod
    def imprimir(texto: str, ancho: int = 40):
        """Imprime cada línea del texto centrada dentro del ancho dado."""
        for linea in texto.splitlines():
            print(linea.center(ancho))

    @staticmethod
    def mostrar(texto: str, ancho: int = 80):
        """Centra en consola el bloque devuelto por un método show_*()."""
        lineas = texto.splitlines()
        ancho_bloque = max((len(k) for k in lineas), default=0)
        padding = max((ancho - ancho_bloque) // 2, 0)
        margen = " " * padding
        for linea in lineas:
            print(margen + linea)

    @staticmethod
    def pregunta(texto: str, ancho: int = 80):
        """Imprime el enunciado de una pregunta centrado con separador."""
        print()
        for linea in texto.strip().splitlines():
            print(linea.center(ancho))
        print()

    @staticmethod
    def respuesta(texto: str = None, ancho: int = 80):
        """Imprime la etiqueta RESPUESTA centrada y el texto si se proporciona."""
        print(Screen.AMARILLO + "RESPUESTA:".center(ancho) + Screen.RESET)
        print()
        if texto:
            for linea in texto.strip().splitlines():
                print(linea.center(ancho))
            print()

    @staticmethod
    def mostrar_grid(bloques: list, columnas: int = 2, ancho_total: int = 80):
        """Muestra bloques de texto en formato grilla (ej: 2x2, 3x1).

        Args:
            bloques    : lista de strings devueltos por show_*()
            columnas   : cuántos bloques por fila (default 2)
            ancho_total: ancho de la consola en caracteres (default 80)
        """
        bloques_lineas = [b.splitlines() for b in bloques]

        for i in range(0, len(bloques_lineas), columnas):
            grupo = bloques_lineas[i:i + columnas]

            max_lineas = max(len(b) for b in grupo)
            ancho_col = ancho_total // columnas
            anchos_bloque = [max((len(k) for k in b), default=0) for b in grupo]

            grupo_norm = [
                b + [""] * (max_lineas - len(b))
                for b in grupo
            ]

            for fila in range(max_lineas):
                fila_txt = ""
                for col_idx, bloque in enumerate(grupo_norm):
                    linea = bloque[fila]
                    ancho_blq = anchos_bloque[col_idx]
                    padding = max((ancho_col - ancho_blq) // 2, 0)
                    celda = (" " * padding + linea).ljust(ancho_col)
                    fila_txt += celda
                print(fila_txt)
            print()
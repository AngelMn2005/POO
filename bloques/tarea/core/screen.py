import os
import shutil


class Screen():

    # Colores ANSI
    ROJO     = "\033[31m"
    VERDE    = "\033[32m"
    AMARILLO = "\033[33m"
    AZUL     = "\033[34m"
    CYAN     = "\033[36m"
    BLANCO   = "\033[97m"
    GRIS     = "\033[37m"
    RESET    = "\033[0m"
    NEGRITA  = "\033[1m"

    # Caracteres del marco
    TL = "╔"
    TR = "╗"
    BL = "╚"
    BR = "╝"
    H  = "═"
    V  = "║"

    @staticmethod
    def _ancho_terminal():
        return shutil.get_terminal_size((100, 24)).columns

    # ──────────────────────────────────────────
    # MÉTODOS BÁSICOS
    # ──────────────────────────────────────────

    @staticmethod
    def limpiar():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def gotoxy(x, y):
        print(f"\033[{y};{x}H", end="")

    @staticmethod
    def pausa():
        input(Screen.GRIS + "\n  Presione Enter para continuar..." + Screen.RESET)

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
    def titulo(texto: str):
        ancho = Screen._ancho_terminal()
        print(Screen.CYAN + Screen.NEGRITA + "═" * ancho + Screen.RESET)
        print(Screen.AZUL + Screen.NEGRITA + texto.center(ancho) + Screen.RESET)
        print(Screen.CYAN + Screen.NEGRITA + "═" * ancho + Screen.RESET)

    @staticmethod
    def tituloExito(texto: str):
        ancho = Screen._ancho_terminal()
        print(Screen.VERDE + Screen.NEGRITA + "═" * ancho + Screen.RESET)
        print(Screen.VERDE + Screen.NEGRITA + texto.center(ancho) + Screen.RESET)
        print(Screen.VERDE + Screen.NEGRITA + "═" * ancho + Screen.RESET)

    @staticmethod
    def pregunta(texto: str, ancho: int = 80):
        print()
        for linea in texto.strip().splitlines():
            print(linea.center(ancho))
        print()

    @staticmethod
    def respuesta(texto: str = None, ancho: int = 80):
        print(Screen.AMARILLO + "RESPUESTA:".center(ancho) + Screen.RESET)
        print()
        if texto:
            for linea in texto.strip().splitlines():
                print(linea.center(ancho))
            print()

    @staticmethod
    def imprimir(texto: str, ancho: int = 40):
        for linea in texto.splitlines():
            print(linea.center(ancho))

    # ──────────────────────────────────────────
    # NÚCLEO: construir marco blanco
    # ──────────────────────────────────────────

    @staticmethod
    def _limpiar_lineas(texto: str) -> list:
        """Elimina separadores internos box-drawing y líneas vacías extremas."""
        separadores = set("━─═╔╗╚╝╠╣║╟╙╘╒╓╫╪┼┤├┬┴┼─│")
        lineas = []
        for h in texto.splitlines():
            s = h.strip()
            chars_unicos = set(s.replace(" ", ""))
            if chars_unicos and chars_unicos.issubset(separadores):
                continue
            lineas.append(s)
        # quitar vacíos extremos
        while lineas and not lineas[0]:
            lineas.pop(0)
        while lineas and not lineas[-1]:
            lineas.pop()
        return lineas

    @staticmethod
    def _construir_marco(lineas: list) -> list:
        """
        Devuelve lista de strings (filas del marco) sin padding de consola.
        El marco usa color blanco brillante.
        """
        C = Screen.BLANCO + Screen.NEGRITA
        R = Screen.RESET

        ancho = max((len(h) for h in lineas), default=0)
        ancho = max(ancho, 28)
        inner = ancho + 2          # espacio izquierdo + derecho

        filas = []
        filas.append(C + Screen.TL + Screen.H * inner + Screen.TR + R)

        for linea in lineas:
            pad = ancho - len(linea)
            filas.append(
                C + Screen.V + R
                + " " + linea + " " * pad + " "
                + C + Screen.V + R
            )

        filas.append(C + Screen.BL + Screen.H * inner + Screen.BR + R)
        return filas

    # ──────────────────────────────────────────
    # mostrar: un solo bloque, centrado
    # ──────────────────────────────────────────

    @staticmethod
    def mostrar(texto: str, ancho: int = None):
        """
        Muestra el bloque de texto dentro de un marco blanco centrado.
        """
        if ancho is None:
            ancho = Screen._ancho_terminal()

        lineas = Screen._limpiar_lineas(texto)
        if not lineas:
            return

        marco = Screen._construir_marco(lineas)

        # ancho real del marco (sin ANSI): max contenido + 2 espacios + 2 bordes
        ancho_marco = max((len(h) for h in lineas), default=28)
        ancho_marco = max(ancho_marco, 28) + 4
        padding = max((ancho - ancho_marco) // 2, 0)
        margen  = " " * padding

        print()
        for fila in marco:
            print(margen + fila)
        print()

    # ──────────────────────────────────────────
    # mostrar_grid: varios marcos en columnas
    # ──────────────────────────────────────────

    @staticmethod
    def mostrar_grid(bloques: list, columnas: int = 2, ancho_total: int = None):
        """
        Muestra cada bloque en su propio marco blanco.
        Los marcos se organizan en 'columnas' columnas, centrados.
        """
        if ancho_total is None:
            ancho_total = Screen._ancho_terminal()

        bloques_lineas = [Screen._limpiar_lineas(b) for b in bloques]

        for i in range(0, len(bloques_lineas), columnas):
            grupo = bloques_lineas[i:i + columnas]
            marcos = [Screen._construir_marco(bl) for bl in grupo]

            # ancho real de cada marco (sin ANSI)
            anchos_reales = []
            for bl in grupo:
                w = max((len(h) for h in bl), default=28)
                anchos_reales.append(max(w, 28) + 4)

            # normalizar altura
            alto_max = max(len(m) for m in marcos)

            def rellenar_marco(marco, ancho_real, alto):
                inner = ancho_real - 2
                C = Screen.BLANCO + Screen.NEGRITA
                R = Screen.RESET
                while len(marco) < alto:
                    fila_vacia = C + Screen.V + R + " " * inner + C + Screen.V + R
                    marco.insert(-1, fila_vacia)
                return marco

            marcos = [rellenar_marco(marcos[j], anchos_reales[j], alto_max)
                    for j in range(len(marcos))]

            # centrar la fila entera
            sep = 3
            ancho_fila = sum(anchos_reales) + sep * (len(grupo) - 1)
            padding_izq = max((ancho_total - ancho_fila) // 2, 0)
            margen = " " * padding_izq

            print()
            for fila_idx in range(alto_max):
                fila_str = margen
                for col_idx, marco in enumerate(marcos):
                    fila_str += marco[fila_idx]
                    if col_idx < len(marcos) - 1:
                        fila_str += " " * sep
                print(fila_str)
            print()

from core import Screen


# ==================================================
# MENU PRINCIPAL
# ==================================================


class Menu:
    def __init__(self, titulo, opciones, width=50):
        self.titulo = titulo
        self.opciones = opciones
        self.width = width

    def draw_box(self, x=35, y=4, limpiar=True):

        if limpiar:
            Screen.limpiar()

        width = self.width

        Screen.gotoxy(x, y)
        print("╔" + "═" * width + "╗")

        Screen.gotoxy(x, y + 1)
        print("║" + self.titulo.center(width) + "║")

        Screen.gotoxy(x, y + 2)
        print("╠" + "═" * width + "╣")

        line = y + 3
        for key, value in self.opciones.items():
            text = f"[{key}] {value['texto']}"
            Screen.gotoxy(x, line)
            print("║ " + text.ljust(width - 1) + "║")
            line += 1

        Screen.gotoxy(x, line)
        print("╚" + "═" * width + "╝")

        return x, line + 2

    def show(self):

        while True:
            x, input_y = self.draw_box()

            Screen.gotoxy(x + 2, input_y)
            option = input("Seleccione una opcion: ").strip()

            if option in self.opciones:
                if option == "0":
                    Screen.limpiar()
                    break

                Screen.limpiar()
                self.opciones[option]["accion"]()

            else:
                Screen.gotoxy(x + 2, input_y + 2)
                Screen.error("Opcion invalida.")
                Screen.pausa()


# ==================================================
# MENU CON PANEL LATERAL
#
# FLUJO:
#   1. Muestra menu izquierdo (bloques)
#   2. Usuario elige bloque → aparece panel derecho (preguntas)
#   3. Usuario elige pregunta → pantalla completa con la pregunta
#   4. Al regresar → solo aparece el panel de preguntas (centrado)
#   5. Usuario presiona 0 → vuelve a los dos paneles
# ==================================================


class MenuConPanel:
    X_IZQ  = 2
    Y_IZQ  = 4
    W_IZQ  = 45

    X_DER  = 52
    Y_DER  = 4
    W_DER  = 42

    X_SOLO = 20
    Y_SOLO = 4
    W_SOLO = 42

    def __init__(self, titulo, opciones):
        self.titulo    = titulo
        self.opciones  = opciones
        self._menu_izq = Menu(titulo, opciones, width=self.W_IZQ)

    def _dibujar_izquierdo(self, limpiar=True):
        return self._menu_izq.draw_box(x=self.X_IZQ, y=self.Y_IZQ, limpiar=limpiar)

    def _dibujar_panel(self, titulo_sub, acciones, x, y, w, limpiar=False):
        """Dibuja una caja de preguntas en la posicion indicada."""
        if limpiar:
            Screen.limpiar()

        titulo_recortado = titulo_sub[:w] if len(titulo_sub) > w else titulo_sub

        Screen.gotoxy(x, y)
        print("╔" + "═" * w + "╗")

        Screen.gotoxy(x, y + 1)
        print("║" + titulo_recortado.center(w) + "║")

        Screen.gotoxy(x, y + 2)
        print("╠" + "═" * w + "╣")

        line = y + 3
        for i in range(len(acciones)):
            text = f"[{i + 1}] Pregunta {i + 1}"
            Screen.gotoxy(x, line)
            print("║ " + text.ljust(w - 1) + "║")
            line += 1

        Screen.gotoxy(x, line)
        print("║ " + "[0] Volver".ljust(w - 1) + "║")
        line += 1

        Screen.gotoxy(x, line)
        print("╚" + "═" * w + "╝")

        return x, line + 2

    def _bucle_preguntas(self, titulo_sub, acciones, modo="doble"):
        """
        modo='doble' → panel derecho junto al izquierdo
        modo='solo'  → panel centrado, sin menu izquierdo
        """
        if modo == "doble":
            x, input_y = self._dibujar_panel(
                titulo_sub, acciones,
                x=self.X_DER, y=self.Y_DER, w=self.W_DER,
                limpiar=False,
            )
        else:
            x, input_y = self._dibujar_panel(
                titulo_sub, acciones,
                x=self.X_SOLO, y=self.Y_SOLO, w=self.W_SOLO,
                limpiar=True,
            )

        while True:
            Screen.gotoxy(x, input_y)
            print(" " * 35, end="")
            Screen.gotoxy(x, input_y)

            sub_opt = input("Opcion: ").strip()

            if sub_opt == "0":
                return "volver"

            try:
                idx = int(sub_opt) - 1
            except ValueError:
                Screen.gotoxy(x, input_y + 2)
                print(" " * 35, end="")
                Screen.gotoxy(x, input_y + 2)
                Screen.error("Opcion invalida.")
                continue

            if 0 <= idx < len(acciones):
                acciones[idx]()

                # Al regresar: mostrar solo el panel de preguntas centrado
                x, input_y = self._dibujar_panel(
                    titulo_sub, acciones,
                    x=self.X_SOLO, y=self.Y_SOLO, w=self.W_SOLO,
                    limpiar=True,
                )
            else:
                Screen.gotoxy(x, input_y + 2)
                print(" " * 35, end="")
                Screen.gotoxy(x, input_y + 2)
                Screen.error("Opcion invalida.")

    def show(self):

        self._dibujar_izquierdo(limpiar=True)
        input_x = self.X_IZQ + 2
        input_y = self.Y_IZQ + 3 + len(self.opciones) + 2

        while True:
            Screen.gotoxy(input_x, input_y)
            print(" " * 40, end="")
            Screen.gotoxy(input_x, input_y)

            option = input("Seleccione una opcion: ").strip()

            if option not in self.opciones:
                Screen.gotoxy(input_x, input_y + 2)
                print(" " * 40, end="")
                Screen.gotoxy(input_x, input_y + 2)
                Screen.error("Opcion invalida.")
                continue

            Screen.gotoxy(input_x, input_y + 2)
            print(" " * 40, end="")

            if option == "0":
                Screen.limpiar()
                break

            datos = self.opciones[option]

            if "preguntas" in datos:
                acciones   = datos["preguntas"]
                titulo_sub = datos["texto"].upper()

                resultado = self._bucle_preguntas(titulo_sub, acciones, modo="doble")

                if resultado == "volver":
                    self._dibujar_izquierdo(limpiar=True)

            elif "accion" in datos:
                datos["accion"]()
                self._dibujar_izquierdo(limpiar=True)
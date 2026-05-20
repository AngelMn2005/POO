from .menu import Menu
from .sub_menu import NivelPrincipiante, NivelIntermedio, NivelAvanzado, NivelPractica


class MenuPrincipal:
    def __init__(self):
        self.principiante = NivelPrincipiante()
        self.intermedio   = NivelIntermedio()
        self.avanzado     = NivelAvanzado()
        self.practica     = NivelPractica()

    def menuPrincipal(self):
        menu = Menu(
            "SISTEMA DE EJERCICIOS PYTHON",
            {
                "1": {
                    "texto": "Nivel Principiante",
                    "accion": self.principiante.show_principiante,
                },
                "2": {
                    "texto": "Nivel Intermedio",
                    "accion": self.intermedio.show_intermedio,
                },
                "3": {
                    "texto": "Nivel Avanzado",
                    "accion": self.avanzado.show_avanzado,
                },
                "4": {
                    "texto": "Nivel Practica",
                    "accion": self.practica.show_practica,
                },
                "0": {
                    "texto": "Salir",
                },
            },
            width=55,
        )
        menu.show()
from .menu import MenuConPanel
from nivel_principiante import Bloque_0, Bloque_1, Bloque_2
from nivel_intermedio import Bloque_3,Bloque_4,Bloque_5,Bloque_6,Bloque_7,Bloque_8,Bloque_9,Bloque_10,Bloque_11
from nivel_avanzado import Bloque_12,Bloque_13,Bloque_14,Bloque_15,Bloque_16,Bloque_17
from nivel_ejercicio_ia import Formulario1,Formulario2,Formulario3,Formulario4,Formulario5


# ==================================================
# NIVEL PRINCIPIANTE
# ==================================================


class NivelPrincipiante:
    def __init__(self):
        self.bloque_0 = Bloque_0()
        self.bloque_1 = Bloque_1()
        self.bloque_2 = Bloque_2()

    def show_principiante(self):
        MenuConPanel(
            "NIVEL PRINCIPIANTE",
            {
                "1": {
                    "texto": "Bloque 0: INTRODUCCION A LA POO",
                    "preguntas": [
                        self.bloque_0.question_1,
                        self.bloque_0.question_2,
                        self.bloque_0.question_3,
                    ],
                },
                "2": {
                    "texto": "Bloque 1: CONSTRUCTOR",
                    "preguntas": [
                        self.bloque_1.b1question_1,
                        self.bloque_1.b1question_2,
                    ],
                },
                "3": {
                    "texto": "Bloque 2: VARIABLES Y TIPOS DE DATOS",
                    "preguntas": [
                        self.bloque_2.b2question_1,
                        self.bloque_2.b2question_2,
                        self.bloque_2.b2question_3,
                    ],
                },
                "0": {"texto": "Volver"},
            },
        ).show()


# ==================================================
# NIVEL INTERMEDIO
# ==================================================


class NivelIntermedio:
    def __init__(self):
        self.bloque_3 = Bloque_3()
        self.bloque_4 = Bloque_4()
        self.bloque_5 = Bloque_5()
        self.bloque_6 = Bloque_6()
        self.bloque_7 = Bloque_7()
        self.bloque_8 = Bloque_8()
        self.bloque_9 = Bloque_9()
        self.bloque_10 = Bloque_10()
        self.bloque_11 = Bloque_11()

    def show_intermedio(self):
        MenuConPanel(
            "NIVEL INTERMEDIO",
            {
                "1": {
                    "texto": "Bloque 3: OPERADORES",
                    "preguntas": [
                        self.bloque_3.b3question_1,
                        self.bloque_3.b3question_2,
                        self.bloque_3.b3question_3,
                    ],
                },
                "2": {
                    "texto": "Bloque 4: ENTRADA Y SALIDA",
                    "preguntas": [
                        self.bloque_4.b4question_1,
                        self.bloque_4.b4question_2,
                        self.bloque_4.b4question_3,
                    ],
                },
                "3": {
                    "texto": "Bloque 5: CONDICIONALES",
                    "preguntas": [
                        self.bloque_5.b5question_1,
                        self.bloque_5.b5question_2,
                        self.bloque_5.b5question_3,
                    ],
                },
                "4": {
                    "texto": "Bloque 6: BUCLES (for / while)",
                    "preguntas": [
                        self.bloque_6.b6question_1,
                        self.bloque_6.b6question_2,
                        self.bloque_6.b6question_3,
                    ],
                },
                "5": {
                    "texto": "Bloque 7: FUNCIONES",
                    "preguntas": [
                        self.bloque_7.b7question_1,
                        self.bloque_7.b7question_2,
                        self.bloque_7.b7question_3,
                    ],
                },
                "6": {
                    "texto": "Bloque 8: LISTAS",
                    "preguntas": [
                        self.bloque_8.b8question_1,
                        self.bloque_8.b8question_2,
                        self.bloque_8.b8question_3,
                    ],
                },
                "7": {
                    "texto": "Bloque 9: TUPLAS",
                    "preguntas": [
                        self.bloque_9.b9question_1,
                        self.bloque_9.b9question_2,
                        self.bloque_9.b9question_3,
                    ],
                },
                "8": {
                    "texto": "Bloque 10: DICCIONARIOS",
                    "preguntas": [
                        self.bloque_10.b10question_1,
                        self.bloque_10.b10question_2,
                        self.bloque_10.b10question_3,
                    ],
                },
                "9": {
                    "texto": "Bloque 11: CONJUNTOS (set)",
                    "preguntas": [
                        self.bloque_11.b11question_1,
                        self.bloque_11.b11question_2,
                        self.bloque_11.b11question_3,
                    ],
                },
                "0": {"texto": "Volver"},
            },
        ).show()


# ==================================================
# NIVEL AVANZADO
# ==================================================


class NivelAvanzado:
    def __init__(self):
        self.bloque_12 = Bloque_12()
        self.bloque_13 = Bloque_13()
        self.bloque_14 = Bloque_14()
        self.bloque_15 = Bloque_15()
        self.bloque_16 = Bloque_16()
        self.bloque_17 = Bloque_17()

    def show_avanzado(self):
        MenuConPanel(
            "NIVEL AVANZADO",
            {
                "1": {
                    "texto": "Bloque 12: EXCEPCIONES (try/except)",
                    "preguntas": [
                        self.bloque_12.b12question_1,
                        self.bloque_12.b12question_2,
                        self.bloque_12.b12question_3,
                    ],
                },
                "2": {
                    "texto": "Bloque 13: DECORADORES",
                    "preguntas": [
                        self.bloque_13.b13question_1,
                        self.bloque_13.b13question_2,
                        self.bloque_13.b13question_3,
                    ],
                },
                "3": {
                    "texto": "Bloque 14: UNPACKING",
                    "preguntas": [
                        self.bloque_14.b14question_1,
                        self.bloque_14.b14question_2,
                        self.bloque_14.b14question_3,
                    ],
                },
                "4": {
                    "texto": "Bloque 15: FUNCIONES DE ORDEN SUPERIOR",
                    "preguntas": [
                        self.bloque_15.b15question_1,
                        self.bloque_15.b15question_2,
                        self.bloque_15.b15question_3,
                    ],
                },
                "5": {
                    "texto": "Bloque 16: ARCHIVOS Y JSON",
                    "preguntas": [
                        self.bloque_16.b16question_1,
                        self.bloque_16.b16question_2,
                        self.bloque_16.b16question_3,
                    ],
                },
                "6": {
                    "texto": "Bloque 17: MIXINS",
                    "preguntas": [
                        self.bloque_17.b17question_1,
                        self.bloque_17.b17question_2,
                        self.bloque_17.b17question_3,
                    ],
                },
                "0": {"texto": "Volver"},
            },
        ).show()


class NivelPractica:
    def __init__(self):
        self.formulario1 = Formulario1()
        self.formulario2 = Formulario2()
        self.formulario3 = Formulario3()
        self.formulario4 = Formulario4()
        self.formulario5 = Formulario5()

    def show_practica(self):
        MenuConPanel(
            "NIVEL AVANZADO",
            {
                "1": {
                    "texto": "Nivel Practica",
                    "preguntas": [
                        self.formulario1.ejecutar,
                        self.formulario2.ejecutar,
                        self.formulario3.ejecutar,
                        self.formulario4.ejecutar,
                        self.formulario5.ejecutar,
                    ],
                },
                
                "0": {"texto": "Volver"},
            },
        ).show()
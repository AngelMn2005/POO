

# Tarea — Programación Orientada a Objetos
### Python · POO · Estructuras de Datos · IA como herramienta de aprendizaje

**Estudiante:** Angel; **Materia:** POO  **Ciudad:** Milagro, Guayas, Ecuador


---

## 📋 Descripción General

Proyecto de ejercicios de **Programación Orientada a Objetos en Python**, organizado en **18 bloques** distribuidos en 3 niveles de dificultad. Cuenta con menú interactivo en consola, validaciones completas en todos los formularios, uso de Mixins, Decoradores, persistencia JSON y exportación de datos.

> 🤖 **Uso de IA documentado:** Se utilizó **Claude (Anthropic)** como herramienta de aprendizaje. Ver todos los prompts en [`docs/prompts.md`](docs/prompts.md)

---

## 🗂️ Estructura del Proyecto

```
tarea/
│
├── 📄 main.py                      ← Punto de entrada
├── 📄 README.md                    ← Esta documentación
│
├── 📁 core/                        ← Módulo de utilidades
│   ├── __init__.py
│   ├── screen.py                   ← Clase Screen (colores, cajas, menús)
│   ├── mixins.py                   ← Mixins reutilizables
│   ├── decorators.py               ← Decoradores Python
│   └── json_manager.py             ← Persistencia JSON
│
├── 📁 views/                       ← Interfaz de usuario
│   ├── menu.py                     ← Clases Menu y MenuConPanel
│   ├── sub_menu.py                 ← Submenús por nivel
│   └── app.py                      ← MenuPrincipal
│
├── 📁 nivel_principiante/          ← Nivel 1 (Bloques 0–2)
├── 📁 nivel_intermedio/            ← Nivel 2 (Bloques 3–11)
├── 📁 nivel_avanzado/              ← Nivel 3 (Bloques 12–17)
├── 📁 nivel_ejercicio_ia/ 
├── 📁 data/                        ← Persistencia
│   ├── data.json
│   ├── users.json
│   └── python.txt
│
└── 📁 docs/                        ← Documentación adicional
    └── prompts.md                  ← Registro de prompts IA
```

---

## ▶️ Cómo Ejecutar

# Requisitos: Python 3.10+ · Terminal con soporte ANSI
python main.py

El programa abre el **menú principal** con 3 niveles. Cada nivel muestra sus bloques y cada bloque sus preguntas.

---

## 🧩 Módulo `core/`

### `screen.py` — Presentación visual

Centraliza todos los colores ANSI y elementos de UI en consola.

| Método | Descripción | Color |
|--------|-------------|-------|
| `Screen.titulo(texto)` | Encabezado con doble línea `══` | Cyan / Azul |
| `Screen.subtitulo(texto)` | Sección secundaria con línea `──` | Amarillo |
| `Screen.enunciado(texto)` | Muestra el enunciado de la pregunta | Amarillo |
| `Screen.respuesta()` | Encabezado de sección RESPUESTA | Verde |
| `Screen.caja(titulo, dict)` | Cuadro con pares clave: valor usando `╔╗╠╣╚╝` | Azul |
| `Screen.resultado(clave, valor)` | Línea `clave → valor` alineada | Cyan / Verde |
| `Screen.lista(items)` | Lista numerada 1. 2. 3. | Blanco |
| `Screen.exito(texto)` | Mensaje ✔ | Verde |
| `Screen.error(texto)` | Mensaje ✘ | Rojo |
| `Screen.aviso(texto)` | Mensaje ⚠ | Amarillo |
| `Screen.pausa()` | "Presione Enter para continuar..." | Blanco |
| `Screen.limpiar()` | Limpia la terminal | — |
| `Screen.gotoxy(x, y)` | Mueve el cursor a posición (x, y) | — |

**Colores disponibles:**
python
Screen.ROJO · Screen.VERDE · Screen.AMARILLO · Screen.AZUL
Screen.CYAN · Screen.BLANCO · Screen.MAGENTA · Screen.RESET · Screen.BOLD


### `mixins.py` — Mixins Reutilizables

Clases que añaden funcionalidad a otras mediante **herencia múltiple**.

#### `ValidationMixin`
python
validar_vacio(valor)        → bool   # False si el campo está vacío
normalizar_texto(texto)     → str    # strip().title()
validar_solo_letras(nombre) → bool   # True si solo contiene letras
validar_precio(valor)       → bool   # True si valor > 0

#### `PromedioMixin`
python
calcular_promedio(notas)    → float  # sum(notas) / len(notas)


#### `ValidacionUsuarioMixin`
python
validar_email(correo)       → bool   # True si tiene "@" y ".com"
validar_edad(edad)          → bool   # True si edad >= 18


#### `ExportarMixin`
python
exportar_json(datos)        → str    # json.dumps con indent=4
exportar_csv(datos)         → str    # valores separados por coma


**Uso con herencia múltiple:**
```python
class MiClase(ValidationMixin, PromedioMixin):
    pass
```

---

### `decorators.py` — Decoradores

| Decorador | Comportamiento |
|-----------|---------------|
| `@iniciar` | Imprime `"Iniciando..."` antes de ejecutar la función |
| `@positivo` | Valida que el argumento sea positivo; retorna `None` si no |
| `@log` | Imprime `"Llamando funcion..."` antes de ejecutar |

```python
@iniciar
def saludo():
    print("Hola mundo")
# → Iniciando...
# → Hola mundo
```

---

### `json_manager.py` — Persistencia JSON

```python
JsonManager.load("data/archivo.json")        # Carga datos (crea el archivo si no existe)
JsonManager.save("data/archivo.json", datos) # Guarda datos con indent=4
```

Crea automáticamente la carpeta `data/` si no existe. Maneja archivos vacíos o corruptos sin lanzar excepción.

---

## 🖥️ Sistema de Menús (`views/`)

```
MenuPrincipal (app.py)
├── [1] Nivel Principiante
│   └── MenuConPanel (sub_menu.py)
│       ├── [1] Bloque 0: Introducción a la POO
│       │   ├── [1] Pregunta 1
│       │   ├── [2] Pregunta 2
│       │   └── [3] Pregunta 3
│       ├── [2] Bloque 1: Constructor
│       └── [3] Bloque 2: Variables
├── [2] Nivel Intermedio
│   └── MenuConPanel
│       ├── [1] Bloque 3  … [9] Bloque 11
├── [3] Nivel Avanzado
│   └── MenuConPanel
│       ├── [1] Bloque 12 … [6] Bloque 17
└── [0] Salir
```

**`Menu`** — Caja simple con opciones y acción directa.  
**`MenuConPanel`** — Dos paneles: izquierdo (bloques) y derecho (preguntas). Al regresar de una pregunta, el panel de preguntas queda centrado solo.

---

## 📚 Ejercicios por Nivel y Bloque

---

## 🟦 NIVEL 1 — PRINCIPIANTE

---

### BLOQUE 0 — Introducción a la POO
**Archivo:** `nivel_principiante/BLOQUE_0.py`  
**Tema:** Clases, objetos e instancias

#### Clases del sistema de biblioteca
```
User      → user_id, name, age, phone
Author    → author_id, name, nationality
Category  → category_id, name
Book      → book_id, title, author, category, pages, available
Loan      → loan_id, user, book, loan_date, status
Person    → name, age
```

| Pregunta | Enunciado | Respuesta clave |
|----------|-----------|----------------|
| P1 | Identifica 5 clases para modelar un sistema de biblioteca | `User, Author, Category, Book, Loan` |
| P2 | Crea la clase `Persona` con nombre y edad; instancia 3 objetos | `person1 = Person("Angel", 18)` |
| P3 | Diferencia entre clase y objeto; ejemplo completo con las 5 clases | Clase = molde · Objeto = instancia |

**IA utilizada — prompts:**
```
P1: "¿Qué es una clase en POO? Cómo identifico clases en un sistema de biblioteca."
P2: "¿Cómo creo __init__ en Python? Muéstrame clase Persona con nombre y edad."
P3: "Explícame con analogía la diferencia entre clase y objeto en Python."
```

---

### BLOQUE 1 — Constructores y Validación
**Archivo:** `nivel_principiante/BLOQUE_1.py`  
**Tema:** `__init__`, validación, `@classmethod`

#### Clases
```python
class Product:          # code, name, price (valida price >= 0)
class Student:          # name, grades=None + @classmethod from_dict()
class Bloque_1(ValidationMixin)
```

| Pregunta | Enunciado | Concepto |
|----------|-----------|---------|
| P1 | Clase `Producto` con validación de precio negativo | `__init__`, `raise ValueError` |
| P2 | Clase `Estudiante` con `@classmethod from_dict()` | `@classmethod`, `cls` |

**IA utilizada — prompts:**
```
P1: "¿Cómo valido parámetros en __init__? Precio no puede ser negativo con raise ValueError."
P2: "¿Para qué sirve @classmethod? Cómo crear objeto desde diccionario con from_dict()."
```

---

### BLOQUE 2 — Variables y Tipos de Datos
**Archivo:** `nivel_principiante/BLOQUE_2.py`  
**Tema:** Tipos simples y complejos, indexación

#### Clases
```python
class Example:    # show_data() — demuestra str, list, dict
class Bloque_2
```

| Pregunta | Enunciado | Tipos usados |
|----------|-----------|-------------|
| P1 | Variable de cada tipo simple y complejo | `str, int, float, bool, list, dict` |
| P2 | Lista de 5 elementos; imprimir primero, último y `[1:4]` | Indexación, slicing |
| P3 | Clase con método que usa str, list y dict | `text[0]`, `name[-1]`, `info['country']` |

**IA utilizada — prompts:**
```
P1: "¿Cuáles son los tipos de datos en Python? Diferencia simples vs complejos."
P2: "¿Cómo accedo al primer y último elemento de una lista? ¿Qué es el slicing?"
P3: "¿Cómo declaro str, list y dict dentro de un método de clase?"
```

---

## 🟪 NIVEL 2 — INTERMEDIO

---

### BLOQUE 3 — Operadores
**Archivo:** `nivel_intermedio/BLOQUE_3.py`

| Pregunta | Enunciado | Concepto |
|----------|-----------|---------|
| P1 | `a=20, b=4` → todos los operadores aritméticos | `+  -  *  /  %  **  //` |
| P2 | Dos listas iguales: `==` es True, `is` es False | Identidad vs igualdad de valor |
| P3 | Evaluar `x = 2 + 1 * 2 % 2 + (2**1)//2` paso a paso | Precedencia de operadores → `x=3` |

**IA utilizada — prompts:**
```
P1: "Explícame todos los operadores aritméticos de Python con a=20 y b=4."
P2: "¿Cuál es la diferencia entre == e is en Python? ¿Por qué listas iguales tienen is=False?"
P3: "¿Cuál es la precedencia de operadores en Python? Evalúa x = 2 + 1 * 2 % 2 + (2**1)//2"
```

---

### BLOQUE 4 — Entrada y Salida
**Archivo:** `nivel_intermedio/BLOQUE_4.py`  
**Hereda:** `ValidationMixin, Screen`

| Pregunta | Enunciado | Validaciones |
|----------|-----------|-------------|
| P1 | Solicita nombre y edad; muestra mensaje con `f-string` | vacío, solo letras, entero > 0 |
| P2 | Lee dos números; calcula suma y promedio | vacío, numérico |
| P3 | Lee temperatura en °C; convierte a °F | vacío, numérico |

**Fórmula P3:** `F = (C × 9/5) + 32`

**IA utilizada — prompts:**
```
P1: "¿Cómo funciona input() en Python? ¿Cómo uso f-strings para mostrar variables?"
P2: "¿Cómo leo dos números y calculo suma y promedio? ¿Qué validaciones debo hacer?"
P3: "¿Cómo convierto Celsius a Fahrenheit en Python? Fórmula y validación de entrada."
```

---

### BLOQUE 5 — Condicionales
**Archivo:** `nivel_intermedio/BLOQUE_5.py`  
**Hereda:** `ValidationMixin`

| Pregunta | Enunciado | Lógica |
|----------|-----------|-------|
| P1 | ¿El número es par o impar? | `n % 2 == 0` |
| P2 | Nota numérica → calificación letra (A/B/C/D/F) | `if/elif/else` con rangos |
| P3 | Dos números + operación (`+  -  *  /`) → resultado | Validación de operador |

**Escala P2:** A≥90 · B≥80 · C≥70 · D≥60 · F<60

**IA utilizada — prompts:**
```
P1: "¿Cómo determino si un número es par o impar en Python?"
P2: "¿Cómo asigno calificación letra con if/elif? Escala A=90, B=80, C=70, D=60."
P3: "¿Cómo valido que el usuario ingrese un operador válido (+,-,*,/) en Python?"
```

---

### BLOQUE 6 — Bucles
**Archivo:** `nivel_intermedio/BLOQUE_6.py`

| Pregunta | Enunciado | Concepto |
|----------|-----------|---------|
| P1 | Imprime números del 1 al 10 con `while` | `while`, contador |
| P2 | Recorre lista de frutas con `enumerate()` | índice + valor |
| P3 | Cuadrados de pares del 1 al 10 | `[n**2 for n in range(1,11) if n%2==0]` |

**Resultado P3:** `[4, 16, 36, 64, 100]`

**IA utilizada — prompts:**
```
P1: "¿Cómo funciona el bucle while? Muéstrame imprimir 1 al 10."
P2: "¿Para qué sirve enumerate()? Cómo mostrar índice y valor de una lista."
P3: "¿Qué es una list comprehension? Cuadrados de pares del 1 al 10 en una línea."
```

---

### BLOQUE 7 — Funciones
**Archivo:** `nivel_intermedio/BLOQUE_7.py`  
**Hereda:** `ValidationMixin`

| Pregunta | Enunciado | Concepto |
|----------|-----------|---------|
| P1 | Función que calcule el doble de un número | `def doble(x): return x * 2` |
| P2 | Suma múltiples argumentos con `*args` | `def suma(*args): return sum(args)` |
| P3 | Factorial recursivo | Caso base `n<=1`, llamada recursiva |

**IA utilizada — prompts:**
```
P1: "¿Cómo defino una función en Python? Muéstrame función que calcule el doble."
P2: "¿Qué es *args en Python? ¿Cómo sumo múltiples argumentos?"
P3: "¿Qué es la recursividad? Explícame el factorial recursivo y su caso base."
```

---

### BLOQUE 8 — Listas
**Archivo:** `nivel_intermedio/BLOQUE_8.py`  
**Hereda:** `ValidationMixin`

| Pregunta | Enunciado | Métodos usados |
|----------|-----------|---------------|
| P1 | Ingresar 3 números, agregar con `append()` y ordenar | `append()`, `sorted()` |
| P2 | Eliminar el 3er elemento e insertar en posición 1 | `pop(2)`, `insert(1, valor)` |
| P3 | Mayor y menor de una lista sin `max()` / `min()` | Recorrido con `for` + comparación |

**IA utilizada — prompts:**
```
P1: "¿Cómo agrego elementos a una lista con append() y la ordeno con sorted()?"
P2: "¿Cómo elimino un elemento por índice con pop() e inserto con insert()?"
P3: "¿Cómo encuentro el mayor y menor de una lista sin usar max() y min()?"
```

---

### BLOQUE 9 — Tuplas
**Archivo:** `nivel_intermedio/BLOQUE_9.py`

| Pregunta | Enunciado | Concepto |
|----------|-----------|---------|
| P1 | Crear tupla e intentar modificarla → `TypeError` | Inmutabilidad |
| P2 | Unpacking con `*rest` → `a, b, *rest = tupla` | Extended unpacking |
| P3 | Recorrer lista de coordenadas con `for x, y in` | Tuple unpacking en bucle |

**IA utilizada — prompts:**
```
P1: "¿Por qué las tuplas son inmutables? ¿Qué error ocurre si intento modificarlas?"
P2: "¿Cómo funciona el unpacking extendido con * en Python?"
P3: "¿Cómo recorro una lista de tuplas desempaquetando en el for?"
```

---

### BLOQUE 10 — Diccionarios
**Archivo:** `nivel_intermedio/BLOQUE_10.py`

| Pregunta | Enunciado | Métodos usados |
|----------|-----------|---------------|
| P1 | Crear diccionario de persona; acceder con `[]` y `.get()` | `dict['key']`, `.get(key, default)` |
| P2 | Iterar con `.items()` mostrando clave y valor | `.items()`, `.keys()`, `.values()` |
| P3 | `copia = datos` → ambas variables apuntan al mismo objeto | Referencia vs copia → `.copy()` |

**IA utilizada — prompts:**
```
P1: "¿Cómo accedo a valores de un diccionario con [] y con get()? ¿Cuál es la diferencia?"
P2: "¿Cómo itero sobre un diccionario mostrando clave y valor con .items()?"
P3: "¿Qué pasa si hago copia = datos en un diccionario? ¿Cómo hago una copia real?"
```

---

### BLOQUE 11 — Conjuntos (Sets)
**Archivo:** `nivel_intermedio/BLOQUE_11.py`

| Pregunta | Enunciado | Operaciones |
|----------|-----------|------------|
| P1 | `A={1,2,3,4}`, `B={3,4,5,6}` → unión, intersección, diferencia | `A\|B`, `A&B`, `A-B` |
| P2 | Eliminar duplicados de `[1,2,2,3,3,3,4]` | `list(set(numbers))` |
| P3 | Calcular `(A\|B) - (A&B)` → diferencia simétrica | Equivale a `A ^ B` |

**IA utilizada — prompts:**
```
P1: "¿Qué es un set en Python? Explícame unión, intersección y diferencia con ejemplos."
P2: "¿Cómo elimino duplicados de una lista usando set en Python?"
P3: "¿Qué es la diferencia simétrica de conjuntos? ¿Cómo se calcula en Python?"
```

---

## 🟩 NIVEL 3 — AVANZADO

---

### BLOQUE 12 — Manejo de Excepciones
**Archivo:** `nivel_avanzado/BLOQUE_12.py`  
**Hereda:** `ValidationMixin`

| Pregunta | Enunciado | Excepción capturada |
|----------|-----------|-------------------|
| P1 | Convertir input a `int`; capturar si el usuario escribe letras | `ValueError` |
| P2 | Acceder a posición de lista; capturar si el índice no existe | `IndexError` |
| P3 | División de dos enteros; capturar ambos tipos de error | `ValueError` + `ZeroDivisionError` |

**IA utilizada — prompts:**
```
P1: "¿Cómo capturo un ValueError al convertir input() a int con try/except?"
P2: "¿Cómo capturo un IndexError al acceder a una posición inválida en una lista?"
P3: "¿Cómo manejo varios tipos de excepción en un solo bloque try con except separados?"
```

---

### BLOQUE 13 — Decoradores
**Archivo:** `nivel_avanzado/BLOQUE_13.py`  
**Importa:** `@iniciar`, `@positivo`, `@log` desde `core`

| Pregunta | Enunciado | Decorador |
|----------|-----------|----------|
| P1 | `@iniciar` → imprime "Iniciando..." antes de `saludo()` | `iniciar` |
| P2 | `@positivo` → valida número > 0 antes de calcular cuadrado | `positivo` |
| P3 | `@log` → registra llamada de `suma(2, 3)` | `log` |

```python
@iniciar
def saludo():
    print("Hola mundo")
# → Iniciando...
# → Hola mundo

@positivo
def cuadrado(n): return n ** 2
# cuadrado(-3) → None (rechazado)
# cuadrado(4)  → 16

@log
def suma(a, b): return a + b
# → Llamando funcion...
# suma(2,3) → 5
```

**IA utilizada — prompts:**
```
P1: "¿Qué es un decorador en Python? Cómo creo uno que imprima algo antes de la función."
P2: "¿Cómo creo un decorador que valide que el argumento sea positivo antes de ejecutar?"
P3: "¿Cómo creo un decorador @log que registre el nombre y argumentos de la función?"
```

---

### BLOQUE 14 — Unpacking Avanzado
**Archivo:** `nivel_avanzado/BLOQUE_14.py`

| Pregunta | Enunciado | Resultado |
|----------|-----------|----------|
| P1 | `first, *middle, last = (10,20,30,40)` | `first=10, middle=[20,30], last=40` |
| P2 | Pasar `[2,3,4]` como argumentos con `*lista` | `multiplicar(*[2,3,4])` = `24` |
| P3 | Combinar dos diccionarios con `**` | `{**data1, **data2}` sin modificar originales |

**IA utilizada — prompts:**
```
P1: "¿Cómo funciona el unpacking extendido con * en Python? Ej: first, *mitad, last."
P2: "¿Cómo paso una lista como argumentos a una función usando * en Python?"
P3: "¿Cómo combino dos diccionarios con ** en Python sin sobrescribir el original?"
```

---

### BLOQUE 15 — Programación Funcional
**Archivo:** `nivel_avanzado/BLOQUE_15.py`  
**Importa:** `reduce` desde `functools`

| Pregunta | Enunciado | Expresión |
|----------|-----------|----------|
| P1 | `map()` para incrementar en 1 cada elemento de `[2,4,6]` | `list(map(lambda x: x+1, nums))` → `[3,5,7]` |
| P2 | `filter()` para obtener los mayores a 3 de `[1,2,3,4,5]` | `list(filter(lambda x: x>3, nums))` → `[4,5]` |
| P3 | `reduce()` para multiplicar todos los elementos de `[1,2,3,4]` | `reduce(lambda a,b: a*b, nums)` → `24` |

**IA utilizada — prompts:**
```
P1: "¿Para qué sirve map() en Python? Muéstrame con lambda para modificar una lista."
P2: "¿Cómo uso filter() con lambda para filtrar elementos de una lista?"
P3: "¿Cómo funciona reduce() de functools? Muéstrame multiplicando todos los elementos."
```

---

### BLOQUE 16 — Persistencia de Datos
**Archivo:** `nivel_avanzado/BLOQUE_16.py`  
**Importa:** `JsonManager`, `os`

| Pregunta | Enunciado | Resultado |
|----------|-----------|----------|
| P1 | Escribe `"Python"` en `data/python.txt` y luego léelo | `open("ruta","w")` + `open("ruta","r")` |
| P2 | Guarda `{"x":10,"y":20}` en JSON y vuelve a cargarlo | `JsonManager.save()` + `JsonManager.load()` |
| P3 | Guarda lista de usuarios en JSON y recorre con `for` | Iteración sobre lista de dicts cargada |

**IA utilizada — prompts:**
```
P1: "¿Cómo escribo y leo un archivo de texto en Python con open()?"
P2: "¿Cómo guardo y cargo un diccionario en formato JSON en Python?"
P3: "¿Cómo guardo una lista de diccionarios en JSON y la recorro con for?"
```

---

### BLOQUE 17 — Proyecto Integrador con Mixins
**Archivo:** `nivel_avanzado/BLOQUE_17.py`  
**Hereda:** `ValidationMixin`

#### Clases del proyecto integrador

```python
class Estudiante(PromedioMixin):
    # nombre, notas
    # mostrar_promedio() → usa calcular_promedio()

class Usuario(ValidacionUsuarioMixin):
    # nombre, correo, edad
    # registrar() → muestra datos + "REGISTRADO"

class Reporte(ExportarMixin):
    # datos (lista de dicts)
    # mostrar_reporte() → exportar_json() + exportar_csv()

class Bloque_17(ValidationMixin):
    # Orquesta las 3 preguntas con entrada de usuario
```

| Pregunta | Enunciado | Mixin usado |
|----------|-----------|------------|
| P1 | `PromedioMixin` → `calcular_promedio(notas)`; integrar en `Estudiante` | `PromedioMixin` |
| P2 | `ValidacionUsuarioMixin` → `validar_email` y `validar_edad`; integrar en `Usuario` | `ValidacionUsuarioMixin` |
| P3 | `ExportarMixin` → `exportar_json` y `exportar_csv`; integrar en `Reporte` | `ExportarMixin` |

**Ejemplo P1:**  
Notas `[8, 9, 10]` → Promedio `9.0`

**Ejemplo P3 — JSON generado:**
```json
[
    {"nombre": "Laptop", "precio": 1200},
    {"nombre": "Mouse",  "precio": 25}
]
```

**IA utilizada — prompts:**
```
P1: "¿Qué son los Mixins en Python? Cómo integro PromedioMixin en una clase Estudiante."
P2: "¿Cómo valido email y edad con un Mixin? Cómo lo integro en una clase Usuario."
P3: "¿Cómo exporto datos a JSON y CSV usando un Mixin con herencia múltiple?"
```

---

## ✅ Validaciones Implementadas

Todos los formularios con entrada de usuario incluyen:

| Tipo | Validación | Método |
|------|-----------|--------|
| Campo vacío | No avanza si el campo está vacío | `validar_vacio()` |
| Solo letras | Nombres solo con caracteres alfabéticos | `validar_solo_letras()` |
| Tipo numérico | Conversión con `try/except ValueError` | Manual |
| Rango de nota | Entre 0 y 10 (o 0 y 100 según contexto) | Comparación `<` / `>` |
| Precio positivo | Mayor a 0 | `validar_precio()` |
| División por cero | `try/except ZeroDivisionError` | Manual |
| Índice inválido | `try/except IndexError` | Manual |
| Email | Contiene `@` y `.com` | `validar_email()` |
| Edad mayor de edad | `>= 18` | `validar_edad()` |

---

## 🤖 Uso de Inteligencia Artificial

**IA utilizada:** Claude — Anthropic ([claude.ai](https://claude.ai))

| Estadística | Valor |
|-------------|-------|
| Total de prompts documentados | 56 |
| Bloques con documentación IA | 18 / 18 |
| Metodología | Explicación → Proceso similar → Resolución propia |

📄 Ver el registro completo en: **[`docs/prompts.md`](docs/prompts.md)**

### Metodología aplicada

```
Para cada ejercicio:
1. Prompt de EXPLICACIÓN    → entender el concepto
2. Prompt de PROCESO SIMILAR → pedir ejercicio parecido para practicar
3. RESOLUCIÓN PROPIA         → resolver sin copiar la respuesta
4. REPETICIÓN hasta comprender completamente
```

---

